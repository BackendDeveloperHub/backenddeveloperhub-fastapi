from fastapi import FastAPI
from routes.health import router as health_router
from routes.ping import router as ping_router
app = FastAPI()
app.include_router(health_router)
app.include_router(ping_router)
@app.get("/")
def read_root():
    return {"msg": "Welcome to the Backend Developer Hub FastAPI!"}