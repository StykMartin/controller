# Proxy to Beaker Server
from typing import Any, Dict, Tuple


def get_recipe(recipe_id: int) -> Dict[str, Any]:
    return {"recipe_id": recipe_id}


def get_recipe_watchdog(recipe_id: int) -> int:
    return recipe_id


def post_recipe_watchdog(recipe_id: int, seconds: int) -> Tuple[int, int]:
    return recipe_id, seconds
