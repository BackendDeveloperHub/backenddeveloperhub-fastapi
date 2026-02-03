from fastapi import FastAPI
from routes.health import router as health_router
app = FastAPI()
app.include_router(health_router)

@app.get("/")
def read_root():
    return {"msg": "Welcome to the Backend Developer Hub FastAPI!"}