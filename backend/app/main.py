from fastapi import FastAPI
from .api.routes import router as api_router
import logging

logger = logging.getLogger(__name__)

app = FastAPI(title="Cardmarket Price Comparison API")


@app.on_event("startup")
async def on_startup() -> None:
    """Log a message when the backend starts."""
    logger.info("Backend API running on http://localhost:8100")


app.include_router(api_router)
