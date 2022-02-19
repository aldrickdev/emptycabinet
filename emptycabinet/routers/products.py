from fastapi import APIRouter

router = APIRouter(prefix="/api/products", tags=["products"])


product_list = [
    {"name": "Beans"},
    {"name": "Bread"},
    {"name": "Milk"},
    {"name": "Eggs"},
]


@router.get("/")
async def get_products():
    return {"Products": product_list}
