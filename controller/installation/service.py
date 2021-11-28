import logging
import re
import shlex
import subprocess  # nosec

logger = logging.getLogger(__name__)

CLEAR_NETBOOT_BIN = "/usr/bin/beaker-clear-netboot"
CLEAR_NETBOOT_CMD = f"sudo {CLEAR_NETBOOT_BIN} {{fqdn}}"

VALID_FQDN_REGEX = (
    r"^(?=.{1,255}$)[0-9A-Za-z]"
    r"(?:(?:[0-9A-Za-z]|\b-){0,61}[0-9A-Za-z])?(?:\.[0-9A-Za-z]"
    r"(?:(?:[0-9A-Za-z]|\b-){0,61}[0-9A-Za-z])?)*\.?$"
)
# do this at the global scope to avoid compiling it on every call
regex_compiled = re.compile(VALID_FQDN_REGEX)


def is_valid_fqdn(fqdn):
    return regex_compiled.search(fqdn)


def clear_netboot(fqdn: str) -> None:
    """Remove netboot configuration for given FQDN."""

    logger.debug("clear_netboot %s", fqdn)

    fqdn_command = CLEAR_NETBOOT_CMD.format(fqdn=fqdn)
    full_command = shlex.split(fqdn_command)

    process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  # nosec
    output, _ = process.communicate()

    if process.returncode:
        raise RuntimeError(f"sudo beaker-clear-netboot failed: {output.strip()}")

    logger.debug("clear_netboot %s completed", fqdn)
