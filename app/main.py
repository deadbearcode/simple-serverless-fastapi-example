from fastapi import FastAPI

from app.api.api_v1.api import router as api_router
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Deployed with CircleCi!"}


app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)