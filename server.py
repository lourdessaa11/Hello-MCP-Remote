# Hello-MCP-Remote/server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-mcp-remote")

@mcp.tool()
def health() -> dict:
    """Liveness check."""
    return {"ok": True, "server": "hello-mcp-remote"}

@mcp.tool()
def echo(msg: str) -> dict:
    """Echoes back your message."""
    return {"echo": msg}

if __name__ == "__main__":
    # Ejecuta el servidor MCP (JSON-RPC sobre stdio)
    mcp.run()
