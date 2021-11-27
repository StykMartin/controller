import logging
import shlex
import subprocess

logger = logging.getLogger(__name__)

CLEAR_NETBOOT_BIN = "/usr/bin/beaker-clear-netboot"
CLEAR_NETBOOT_CMD = f"sudo {CLEAR_NETBOOT_BIN} {{fqdn}}"


def clear_netboot(fqdn: str) -> None:
    """Remove netboot configuration for given FQDN."""

    logger.debug("clear_netboot %s", fqdn)

    fqdn_command = CLEAR_NETBOOT_CMD.format(fqdn=fqdn)
    full_command = shlex.split(fqdn_command)

    process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, _ = process.communicate()

    if process.returncode:
        raise RuntimeError(f"sudo beaker-clear-netboot failed: {output.strip()}")

    logger.debug("clear_netboot %s completed", fqdn)
