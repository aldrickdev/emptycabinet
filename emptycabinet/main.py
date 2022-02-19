from fastapi import FastAPI
from emptycabinet.routers import products


app = FastAPI()

app.include_router(products.router)


@app.get("/")
def index():
    return {"Endpoints": ["/api/products"]}
