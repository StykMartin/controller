from fastapi import APIRouter
from starlette.responses import JSONResponse

from controller.health.view import health_router
from controller.installation.view import installation_router
from controller.recipe.view import recipe_router

api_router = APIRouter(default_response_class=JSONResponse)

api_router.include_router(health_router, prefix="/health", tags=["Health"])
api_router.include_router(recipe_router, prefix="/recipes", tags=["Recipes"])
api_router.include_router(installation_router, tags=["Installation"])
