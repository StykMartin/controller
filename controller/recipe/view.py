from fastapi import APIRouter

recipe_router = APIRouter()


@recipe_router.get("/{recipe_id}")
def get_recipe(recipe_id: int):
    return recipe_id


@recipe_router.get("/{recipe_id}/watchdog")
def get_recipe_watchdog(recipe_id: int):
    return recipe_id


@recipe_router.post("/{recipe_id}/watchdog")
def post_recipe_watchdog(recipe_id: int):
    pass


@recipe_router.post("/{recipe_id}/status")
def post_recipe_status(recipe_id: int):
    pass


@recipe_router.patch("/{recipe_id}/tasks/{task_id}")
def patch_recipe_task(recipe_id: int, task_id: int):
    pass


@recipe_router.post("/{recipe_id}/tasks/{task_id}/status")
def post_task_status(recipe_id: int, task_id: int):
    pass


@recipe_router.post("/{recipe_id}/tasks/{task_id}/results")
def post_task_results(recipe_id: int, task_id: int):
    pass


@recipe_router.get("/{recipe_id}/logs")
def get_recipe_logs(recipe_id: int):
    pass


@recipe_router.get("/{recipe_id}/logs/{path:path}")
def get_recipe_log(recipe_id: int, path):
    pass


@recipe_router.post("/{recipe_id}/logs/{path:path}")
def post_recipe_log(recipe_id: int, path):
    pass


@recipe_router.get("/{recipe_id}/tasks/{task_id}/logs")
def get_task_logs(recipe_id: int, task_id: int):
    pass


@recipe_router.get("/{recipe_id}/tasks/{task_id}/logs/{path:path}")
def get_task_log(recipe_id: int, task_id: int, path):
    pass


@recipe_router.put("/{recipe_id}/tasks/{task_id}/logs/{path:path}")
def put_task_log(recipe_id: int, task_id: int, path):
    pass


@recipe_router.get("/{recipe_id}/tasks/{task_id}/results/{result_id:int}/logs")
def get_task_result_logs(recipe_id: int, task_id: int, result_id):
    pass


@recipe_router.get("/{recipe_id}/tasks/{task_id}/results/{result_id:int}/logs/{path:path}")
def get_task_result_log(recipe_id: int, task_id: int, result_id, path):
    pass


@recipe_router.put("/{recipe_id}/tasks/{task_id}/results/{result_id:int}/logs/{path:path}")
def put_task_result_log(recipe_id: int, task_id: int, result_id, path):
    pass
