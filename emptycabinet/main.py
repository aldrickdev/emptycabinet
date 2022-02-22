from fastapi import FastAPI

from emptycabinet.routers import users, products
from emptycabinet.dependencies import user_auth

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)
app.include_router(user_auth.router)


@app.get("/")
def index():
    return {"Hello": "World"}
