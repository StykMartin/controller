from fastapi import APIRouter, HTTPException
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

from controller.installation.service import clear_netboot

installation_router = APIRouter()


@installation_router.get("/nopxe/{fqdn}")
def get_no_pxe(fqdn: str):
    """Called from kickstart post section to remove netboot entry."""
    try:
        clear_netboot(fqdn)
    except RuntimeError:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Unable to perform clear netboot for FQDN {fqdn}",
        )
    return Response(status_code=HTTP_204_NO_CONTENT)


@installation_router.get("/install_start/{recipe_id}")
def get_install_start(recipe_id: int):
    pass


@installation_router.get("/install_done/{recipe_id}")
@installation_router.get("/install/done/{recipe_id}/{fqdn}")
def get_install_done(recipe_id: int, _):
    pass


@installation_router.get("/postinstall_done/{recipe_id}")
def get_post_install_done(recipe_id: int):
    pass


@installation_router.get("/postreboot/{recipe_id}")
def get_post_reboot(recipe_id: int):
    pass


@installation_router.get("/install_fail/{recipe_id}")
def get_install_fail(recipe_id: int):
    pass
