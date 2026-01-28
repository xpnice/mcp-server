# coding:utf-8

from src.imagex.mcp_server import create_mcp_server
from dotenv import load_dotenv
import asyncio
import sys
import argparse
import logging

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run the veImageX MCP Server")
    parser.add_argument(
        "--transport", "-t",
        choices=["sse", "stdio", "streamable-http"],
        default="stdio",
        help="Transport protocol to use (sse, stdio, or streamable-http)"
    )
    parser.add_argument("--host", help="Host to bind to for HTTP transports")
    parser.add_argument("--port", type=int, help="Port to bind to for HTTP transports")
    args = parser.parse_args()

    try:
        mcp = create_mcp_server()
        
        logger.info("Starting MCP Server veImageX with %s transport", args.transport)
        
        if args.transport == "stdio":
            asyncio.run(mcp.run(transport="stdio"))
        else:
            # Only pass host and port if they were explicitly provided via CLI
            run_kwargs = {"transport": args.transport}
            if args.host:
                run_kwargs["host"] = args.host
            if args.port:
                run_kwargs["port"] = args.port
            
            asyncio.run(mcp.run(**run_kwargs))
    except Exception as e:
        logger.error(f"Error starting veImageX MCP Server: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
