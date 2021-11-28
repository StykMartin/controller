# Proxy to Beaker Server
import typing


def get_recipe(recipe_id: int) -> typing.Dict:
    return {"recipe_id": recipe_id}


def get_recipe_watchdog(recipe_id: int) -> int:
    return recipe_id


def post_recipe_watchdog(recipe_id: int, seconds: int):
    return recipe_id, seconds
