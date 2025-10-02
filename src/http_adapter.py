from fastapi import FastAPI
import subprocess
import json

app = FastAPI(title="AWS CLI MCP Adapter")

@app.post("/generate")
async def generate(input: dict):
    # Call MCP server in subprocess (IPC bridge)
    proc = subprocess.Popen(
        ["python3", "mcp_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    req = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "generate_aws_cli",
        "params": {"input": input["text"]}
    }
    out, _ = proc.communicate(json.dumps(req))
    return json.loads(out)
