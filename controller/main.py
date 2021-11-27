"""Entry point for API/PROXY"""

import time
from urllib.request import Request

import uvicorn
from fastapi import FastAPI

from controller.api import api_router

app = FastAPI(
    title="Controller",
    swagger_ui_oauth2_redirect_url=None,
    description="Beaker controller",
)

app.include_router(api_router)


@app.middleware("http")
async def add_headers(request: Request, call_next):
    """Expose process time in each request."""

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


if __name__ == "__main__":
    uvicorn.run(  # pragma: no cover
        f"{__name__}:app", host="127.0.0.1", port=8000, use_colors=True, reload=False
    )
