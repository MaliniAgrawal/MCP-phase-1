import asyncio
import logging
import sys
from loguru import logger

# Configure stdlib logging to stderr so JSON-RPC on stdout isn't polluted
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

# Configure loguru to stderr as well
logger.remove()
logger.add(sys.stderr, level="INFO")

from fastmcp import FastMCP
from core.command_generator import generate_command


# Create MCP server
mcp = FastMCP("aws-cli-generator")

# Some third-party logging config (e.g. FastMCP's RichHandler) may have been
# added after import. To guarantee the MCP protocol keeps stdout clean, make
# sure all root logging handlers write to stderr. This adjusts common handler
# attributes (stream) and RichHandler's console to use stderr.
try:
    import logging
    from rich.console import Console

    root_logger = logging.getLogger()
    for h in list(root_logger.handlers):
        try:
            # If handler has a console (RichHandler), replace it with one that
            # writes to stderr explicitly.
            if hasattr(h, "console"):
                h.console = Console(file=sys.stderr, force_terminal=False)
            # If handler writes to a stream attribute, ensure it's stderr.
            if hasattr(h, "stream"):
                try:
                    h.stream = sys.stderr
                except Exception:
                    pass
        except Exception:
            # be conservative: don't fail startup due to logging adjustments
            continue
except Exception:
    pass


# Tool: Generate AWS CLI command
@mcp.tool()
async def generate_aws_cli(nl_request: str) -> dict:
    """
    Convert natural language into an AWS CLI command with explanation.
    """
    try:
        cli, explanation = generate_command(nl_request)
        return {"command": cli, "explanation": explanation}
    except Exception as e:
        logger.exception("Error generating command")
        return {"error": str(e)}

async def main():
    logger.info("Starting MCP stdio server (aws-cli-generator)")
    await mcp.run_stdio_async()

if __name__ == "__main__":
    asyncio.run(main())
