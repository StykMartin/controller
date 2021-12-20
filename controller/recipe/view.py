from typing import Any, Dict

from fastapi import APIRouter, Form
from starlette.responses import Response

from controller.recipe import model as recipe_model
from controller.recipe import service as recipe_service
from controller.response import XMLResponse

recipe_router = APIRouter()


@recipe_router.get("/{recipe_id}", response_class=XMLResponse)
def get_recipe(recipe_id: int) -> Dict[str, Any]:

    response = recipe_service.get_recipe(recipe_id)
    return response


@recipe_router.get("/{recipe_id}/watchdog")
def get_recipe_watchdog(recipe_id: int) -> recipe_model.WatchdogRead:
    """Return watchdog value in seconds for given Recipe."""

    seconds = recipe_service.get_recipe_watchdog(recipe_id)

    return recipe_model.WatchdogRead(seconds=seconds)


@recipe_router.post("/{recipe_id}/watchdog")
def post_recipe_watchdog(recipe_id: int, seconds: int = Form(...)) -> Response:

    recipe_service.post_recipe_watchdog(recipe_id, seconds)

    return Response(status_code=204)


@recipe_router.post("/{recipe_id}/status")
def post_recipe_status(recipe_id: int, status: str = Form(..., example="aborted", regex="aborted")) -> Response:
    """Allow aborting recipe via API.
    All other operations are not allowed via API as they are managed in the scheduler.
    """

    return Response(status_code=204)


@recipe_router.patch("/{recipe_id}/tasks/{task_id}")
def patch_recipe_task(recipe_id: int, task_id: int) -> None:
    pass


@recipe_router.post("/{recipe_id}/tasks/{task_id}/status")
def post_task_status(recipe_id: int, task_id: int) -> None:
    pass


@recipe_router.post("/{recipe_id}/tasks/{task_id}/results")
def post_task_results(recipe_id: int, task_id: int) -> None:
    pass


@recipe_router.get("/{recipe_id}/logs")
def get_recipe_logs(recipe_id: int) -> None:
    pass


@recipe_router.get("/{recipe_id}/logs/{path:path}")
def get_recipe_log(recipe_id: int, path: str) -> None:
    pass


@recipe_router.post("/{recipe_id}/logs/{path:path}")
def post_recipe_log(recipe_id: int, path: str) -> None:
    pass


@recipe_router.get("/{recipe_id}/tasks/{task_id}/logs")
def get_task_logs(recipe_id: int, task_id: int) -> None:
    pass


@recipe_router.get("/{recipe_id}/tasks/{task_id}/logs/{path:path}")
def get_task_log(recipe_id: int, task_id: int, path: str) -> None:
    pass


@recipe_router.put("/{recipe_id}/tasks/{task_id}/logs/{path:path}")
def put_task_log(recipe_id: int, task_id: int, path: str) -> None:
    pass


@recipe_router.get("/{recipe_id}/tasks/{task_id}/results/{result_id:int}/logs")
def get_task_result_logs(recipe_id: int, task_id: int, result_id: int) -> None:
    pass


@recipe_router.get("/{recipe_id}/tasks/{task_id}/results/{result_id:int}/logs/{path:path}")
def get_task_result_log(recipe_id: int, task_id: int, result_id: int, path: str) -> None:
    pass


@recipe_router.put("/{recipe_id}/tasks/{task_id}/results/{result_id:int}/logs/{path:path}")
def put_task_result_log(recipe_id: int, task_id: int, result_id: int, path: str) -> None:
    pass
