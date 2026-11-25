import os
import sys
import time
import json
import subprocess
import urllib.request
import urllib.error

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VENV_PYTHON = os.path.join(ROOT_DIR, '.venv', 'bin', 'python')
VENV_JUPYTER = os.path.join(ROOT_DIR, '.venv', 'bin', 'jupyter')
CONFIG_PATH = os.path.join(ROOT_DIR, 'jupyter_server_config.py')
SANDBOX_PATH = os.path.join(ROOT_DIR, 'library', 'test', 'sandbox.ipynb')
API_URL = 'http://127.0.0.1:8888/api'
TOKEN = 'sahacit-dev'

def make_req(path, method='GET', data=None):
    url = f"{API_URL}{path}?token={TOKEN}"
    req = urllib.request.Request(url, method=method)
    if data is not None:
        req.add_header('Content-Type', 'application/json')
        body = json.dumps(data).encode('utf-8')
        req.data = body
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
        return json.loads(content) if content else {}

def main():
    print("==================================================")
    print(" Running sahacit Phase 1 & 2 Substrate Verification")
    print("==================================================")

    # 1. Start Jupyter Server
    print("[1/5] Launching Jupyter Server on port 8888...")
    proc = subprocess.Popen(
        [VENV_JUPYTER, 'server', f'--config={CONFIG_PATH}'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    try:
        # Wait for server readiness
        connected = False
        for i in range(25):
            time.sleep(0.4)
            try:
                res = make_req('/status')
                if res.get('started'):
                    connected = True
                    print(f"  ✓ Jupyter Server ready (version {res.get('version')})")
                    break
            except Exception:
                pass

        if not connected:
            raise RuntimeError("Could not connect to Jupyter Server within 10s")

        # 2. Test Contents API Listing
        print("[2/5] Testing Contents API directory listing...")
        root_contents = make_req('/contents')
        print(f"  ✓ Root contents found: {[item['name'] for item in root_contents.get('content', [])]}")
        
        test_dir = make_req('/contents/test')
        files = [item['name'] for item in test_dir.get('content', [])]
        print(f"  ✓ /test directory contents: {files}")
        assert 'sandbox.ipynb' in files, "sandbox.ipynb not found in /test"

        # 3. Read Notebook Model
        print("[3/5] Fetching test/sandbox.ipynb via REST...")
        nb_model = make_req('/contents/test/sandbox.ipynb')
        cells = nb_model.get('content', {}).get('cells', [])
        print(f"  ✓ Loaded notebook successfully ({len(cells)} cells)")
        initial_mod_time = nb_model.get('last_modified')

        # 4. Start Kernel Session
        print("[4/5] Starting kernel session for sandbox.ipynb...")
        session_payload = {
            'name': 'test/sandbox.ipynb',
            'path': 'test/sandbox.ipynb',
            'type': 'notebook',
            'kernel': {'name': 'python3'}
        }
        session = make_req('/sessions', method='POST', data=session_payload)
        session_id = session['id']
        kernel_id = session['kernel']['id']
        print(f"  ✓ Kernel session active! Session ID: {session_id[:8]}..., Kernel ID: {kernel_id[:8]}...")

        # 5. Test External Mutation Detection
        print("[5/5] Testing external modification detection (simulating AI agent)...")
        with open(SANDBOX_PATH, 'r', encoding='utf-8') as f:
            nb_json = json.load(f)

        test_msg = "# Added by automated verification agent"
        nb_json['cells'].append({
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'outputs': [],
            'source': [test_msg]
        })

        time.sleep(0.5)
        with open(SANDBOX_PATH, 'w', encoding='utf-8') as f:
            json.dump(nb_json, f, indent=1)

        # Query REST API again
        updated_model = make_req('/contents/test/sandbox.ipynb')
        new_mod_time = updated_model.get('last_modified')
        updated_cells = updated_model.get('content', {}).get('cells', [])
        
        print(f"  ✓ Initial last_modified: {initial_mod_time}")
        print(f"  ✓ New last_modified:     {new_mod_time}")
        print(f"  ✓ Updated cell count:     {len(updated_cells)}")
        assert new_mod_time != initial_mod_time, "last_modified timestamp did not update!"
        assert len(updated_cells) == len(cells) + 1, "New cell was not returned by Contents API!"

        # Clean up added test cell
        nb_json['cells'].pop()
        with open(SANDBOX_PATH, 'w', encoding='utf-8') as f:
            json.dump(nb_json, f, indent=1)

        # Delete session
        make_req(f'/sessions/{session_id}', method='DELETE')
        print("  ✓ Kernel session cleanly disposed.")

        print("\n==================================================")
        print(" 🎉 All Substrate & Canvas Engine Tests PASSED!")
        print("==================================================")

    finally:
        proc.kill()

if __name__ == '__main__':
    main()
