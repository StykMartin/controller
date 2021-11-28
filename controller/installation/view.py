from fastapi import APIRouter, HTTPException
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

from controller.installation import service as installation_service

installation_router = APIRouter()

BROKEN_NETBOOT = HTTPException(
    status_code=HTTP_400_BAD_REQUEST,
    detail=f"Unable to perform clear netboot for given FQDN",
)


@installation_router.get("/nopxe/{fqdn}")
def get_no_pxe(fqdn: str):
    """Called from kickstart post section to remove netboot entry."""

    u_fqdn = fqdn.strip()

    if not installation_service.is_valid_fqdn(u_fqdn):
        raise BROKEN_NETBOOT

    try:
        installation_service.clear_netboot(u_fqdn)
    except RuntimeError:
        raise BROKEN_NETBOOT
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
