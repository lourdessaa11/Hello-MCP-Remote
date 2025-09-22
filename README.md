# Hello-MCP-Remote (trivial)

Minimal MCP server exposing two tools:
- `health()` → returns `{ok:true, server:"hello-mcp-remote"}`
- `echo(msg)` → returns `{echo: "<msg>"}`

## Run (local)
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python server.py
