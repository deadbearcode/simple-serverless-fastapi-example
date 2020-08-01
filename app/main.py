from fastapi import FastAPI

from app.api.api_v1.api import router as api_router
from app.core.config import settings
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Secret Key: {settings.SECRET_KEY}"}


app.include_router(api_router, prefix=settings.API_V1_STR)
handler = Mangum(app)