from fastapi import FastAPI
from routes.test_routes import router

app = FastAPI()

app.include_router(router)