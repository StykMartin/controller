from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("/")
@health_router.head("/")
def get_health() -> str:
    return "Healthy!"
