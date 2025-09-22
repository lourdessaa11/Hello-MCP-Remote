# app.py (en la raíz de Hello-MCP-Remote)
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Any, Dict, Optional
import uvicorn

app = FastAPI(title="hello-mcp-remote-http")

# Tools triviales (mismo comportamiento que server.py)
def tool_health() -> Dict[str, Any]:
    return {"ok": True, "server": "hello-mcp-remote"}

def tool_echo(msg: str) -> Dict[str, Any]:
    return {"echo": msg}

# Modelo mínimo JSON-RPC 2.0
class JsonRpcRequest(BaseModel):
    jsonrpc: str
    method: str
    params: Optional[Dict[str, Any]] = None
    id: Optional[Any] = None

@app.post("/rpc")
async def rpc_endpoint(req: Request):
    body = await req.json()
    try:
        data = JsonRpcRequest(**body)
    except Exception:
        return {"jsonrpc": "2.0", "error": {"code": -32700, "message": "Parse error"}, "id": None}

    # Solo respondemos a jsonrpc "2.0"
    if data.jsonrpc != "2.0":
        return {"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": data.id}

    try:
        if data.method == "health":
            result = tool_health()
        elif data.method == "echo":
            msg = (data.params or {}).get("msg", "")
            result = tool_echo(msg)
        else:
            return {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": data.id}
        return {"jsonrpc": "2.0", "result": result, "id": data.id}
    except Exception as e:
        return {"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}, "id": data.id}

if __name__ == "__main__":
    uvicorn.run("app:rpc_endpoint", host="0.0.0.0", port=8080)
