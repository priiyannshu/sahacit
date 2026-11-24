#!/bin/bash
set -e

JUPYTER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$JUPYTER_DIR")"
NOTEBOOK_PATH="${1:-$JUPYTER_DIR/library/test/sandbox.ipynb}"

echo "=================================================="
echo " Starting sahacit Engine & AI Tutor"
echo " Active Notebook: $NOTEBOOK_PATH"
echo "=================================================="

# 1. Clean up any existing instances or blocked ports
echo "Checking ports 8888 and 5173..."
fuser -k 8888/tcp 2>/dev/null || true
fuser -k 5173/tcp 2>/dev/null || true
sleep 1

# 2. Start Jupyter Server
if [ -f "$JUPYTER_DIR/.venv/bin/activate" ]; then
  source "$JUPYTER_DIR/.venv/bin/activate"
elif [ -f "$REPO_DIR/.venv/bin/activate" ]; then
  source "$REPO_DIR/.venv/bin/activate"
fi
jupyter server --config="$JUPYTER_DIR/jupyter_server_config.py" > "$JUPYTER_DIR/jupyter.log" 2>&1 &
JUPYTER_PID=$!
echo "✓ Jupyter Server started on port 8888 (PID $JUPYTER_PID)"

# Wait for Jupyter Server to respond
for i in {1..15}; do
  if python3 -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8888/api/status?token=sahacit-dev')" 2>/dev/null; then
    echo "✓ Jupyter Server is healthy and responsive."
    break
  fi
  sleep 0.5
done

# 3. Start Frontend (Vite)
cd "$REPO_DIR/web"
npm run dev > "$JUPYTER_DIR/vite.log" 2>&1 &
VITE_PID=$!
echo "✓ Vite Frontend started on port 5173 (PID $VITE_PID)"

# Wait for Vite frontend to respond
for i in {1..15}; do
  if python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:5173')" 2>/dev/null; then
    echo "✓ Frontend is live at http://localhost:5173"
    break
  fi
  sleep 0.5
done

# 4. Launch Antigravity Tutor in a dedicated tmux session
TMUX_SESSION="sahacit-tutor"
if tmux has-session -t "$TMUX_SESSION" 2>/dev/null; then
  echo "Terminating prior $TMUX_SESSION tmux session..."
  tmux kill-session -t "$TMUX_SESSION"
fi

echo "Launching Antigravity AI Tutor in tmux session '$TMUX_SESSION'..."
tmux new-session -d -s "$TMUX_SESSION" -c "$REPO_DIR" \
  "agy --dangerously-skip-permissions -i 'tutor watch $NOTEBOOK_PATH' ; bash"

echo "✓ AI Tutor is running and watching the notebook!"
echo ""
echo "=================================================="
echo " 🚀 MVP Loop is Live!"
echo " • Web UI:       http://localhost:5173"
echo " • Jupyter API:  http://127.0.0.1:8888"
echo " • Tutor Agent:  tmux attach -t sahacit-tutor"
echo "=================================================="
echo "Press Ctrl+C to stop all servers and tutor agent."

# Clean exit handler
cleanup() {
  echo ""
  echo "Shutting down sahacit..."
  kill $JUPYTER_PID $VITE_PID 2>/dev/null || true
  tmux kill-session -t "$TMUX_SESSION" 2>/dev/null || true
  fuser -k 8888/tcp 2>/dev/null || true
  fuser -k 5173/tcp 2>/dev/null || true
  echo "All processes cleanly stopped."
  exit 0
}

trap cleanup SIGINT SIGTERM
wait
