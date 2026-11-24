# NotebookLM Programmatic Access Tools

Two candidates for programmatic access to Google Gemini NotebookLM (formerly NotebookLM):

## 1. `notebooklm-py` (v0.8.1)

**Package**: `notebooklm-py` | **PyPI**: https://pypi.org/project/notebooklm-py/

**Primary approach**: Python library + CLI + MCP server + REST server

**Key capabilities**:
- **Python API** — Full programmatic access: create notebooks, add sources (URLs, YouTube, Google Drive, files), chat with sources, generate content (audio podcasts, videos, slide decks, quizzes, flashcards, infographics, reports, data tables, mind maps), download artifacts
- **CLI** — `notebooklm` command with full feature set: `create`, `source add`, `ask`, `generate audio/video/quiz/etc.`, `download`
- **MCP server** — Model Context Protocol server for AI assistant integration (Claude Code, Cursor, Gemini CLI, etc.)
- **REST server** — FastAPI-based localhost server for HTTP access
- **Authentication** — Playwright browser login, browser cookies import, or master-token auth. Chromium download (~170MB) on first login
- **Extras**: `browser`, `mcp`, `server`, `headless`, `impersonate`, `markdown` extras

**Install**: `uv tool install "notebooklm-py[browser]"` or `pip install notebooklm-py` (inside venv)

**CLI binaries provided**: `notebooklm`, `notebooklm-mcp`, `notebooklm-server`

**Best for**: Application integration, research automation, content generation pipelines, custom Python scripts

---

## 2. `notebooklm-mcp-cli` (v0.9.12)

**Package**: `notebooklm-mcp-cli` | **PyPI**: https://pypi.org/project/notebooklm-mcp-cli/

**Primary approach**: Unified CLI + MCP server (single package)

**Key capabilities**:
- **CLI** — `nlm` command: `notebook list`, `notebook create`, `source add`, `audio create`, `download`, `share`, `research`, `studio create`
- **MCP server** — 43 tools for AI assistants (Claude Desktop, Claude Code, Cursor, Gemini, GitHub Copilot, etc.) with automatic setup via `nlm setup add <tool>`
- **Authentication** — Browser-based cookie extraction (Chrome, Arc, Brave, Edge, Firefox, Chromium). Profile management for multiple Google accounts
- **Setup** — `nlm setup add/remove/list` for AI tool integration; `nlm doctor` for diagnostics
- **MCP tools** — `notebook_list`, `notebook_create`, `source_add`, `notebook_query`, `studio_create`, `download_artifact`, `research_start`, `chat_list`, etc.
- **Authentication lifecycle** — Cookies last ~2-4 weeks, auto-refresh supported

**Install**: `uv tool install notebooklm-mcp-cli` or `pipx install notebooklm-mcp-cli`

**CLI binaries provided**: `nlm`, `notebooklm-mcp`

**Best for**: AI assistant integration (Claude Code, Cursor, Gemini CLI), quick scripts, MCP workflows, cross-tool compatibility

---

## Comparison Summary

| Aspect | `notebooklm-py` | `notebooklm-mcp-cli` |
|---|---|---|
| **Primary interface** | Python API + CLI | CLI + MCP server |
| **MCP tools** | Custom MCP server (3-entry points) | 43-tools MCP server |
| **Content generation** | Full suite (audio, video, slides, quizzes, flashcards, mind maps, reports, data tables) | Core generation via MCP tools |
| **Source management** | URLs, YouTube, Drive, files, pasted text | URLs, files, Drive |
| **Authentication** | Playwright Chromium, browser cookies, master-token | Browser CDP (Chrome/Firefox), profile management |
| **AI assistant ready** | Via MCP server or REST server | Out-of-the-box via `nlm setup add` |
| **CLI binaries** | `notebooklm`, `notebooklm-mcp`, `notebooklm-server` | `nlm`, `notebooklm-mcp` |
| **Python version** | >=3.10 | >=3.11 |

---

## Coexistence Note

Both packages provide a `notebooklm-mcp` executable, causing a name collision. This was resolved by:
- `notebooklm-mcp-cli` owns the `notebooklm-mcp` binary (installed via `uv tool install --force`)
- `notebooklm-py` is installed into its own venv (`~/.local/share/notebooklm-py`), with only `notebooklm` + `notebooklm-server` symlinked to `~/.local/bin`
- `notebooklm-py`'s MCP server can be run on-demand: `uvx --from notebooklm-py notebooklm-mcp`

## Quickstart — Authentication

Both require initial auth:

```bash
# notebooklm-py
notebooklm login          # launches browser, downloads Chromium, extracts cookies

# notebooklm-mcp-cli
nlm login                 # launches browser, extracts cookies
```

Cookies persist ~2-4 weeks; refresh with `notebooklm auth refresh --quiet` or `nlm login --check`.

## Which one should you use?

- Use **`notebooklm-py`** if you want Python API integration, custom pipelines, research automation, or need the full content generation suite (especially quiz/flashcard/mind map export in multiple formats).
- Use **`notebooklm-mcp-cli`** if you work with AI assistants (Claude Code, Cursor, Gemini CLI), want MCP tool integration, or prefer CLI-first workflows without Python code.
- Keep **both** if you need both Python integration AND AI-assistant/MCP workflows — they complement each other despite the shared MCP binary name.