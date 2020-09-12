from fastapi import FastAPI
from mangum import Mangum
from app.core import config

from app.api.api_v1.api import router as api_router


app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"This is our secret key value: {config.settings.secret_key}" }


app.include_router(api_router, prefix=config.settings.prefix)
handler = Mangum(app)
