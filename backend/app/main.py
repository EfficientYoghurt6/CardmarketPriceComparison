from fastapi import FastAPI
from .api.routes import router as api_router

app = FastAPI(title="Cardmarket Price Comparison API")

app.include_router(api_router)
