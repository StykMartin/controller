"""Configuration for Controller"""

from starlette.config import Config

config = Config("/etc/beaker/labcontroller.conf")

# Process pid file.
PROXY_PID_FILE = config(
    "BEAKER_PROXY_PID_FILE", default="/var/run/beaker-lab-controller/beaker-proxy.pid"
)

# How long to sleep between polls.
SLEEP_TIME = config("BEAKER_POOL_SLEEP_TIME", cast=int, default=20)

# Timeout for fetching distro images.
IMAGE_FETCH_TIMEOUT = config("BEAKER_IMAGE_FETCH_TIMEOUT", cast=int, default=120)

# Number of times to attempt failing power commands.
POWER_ATTEMPTS = config("BEAKER_POWER_ATTEMPS", cast=int, default=5)

# Location of locally stored job logs
CACHEPATH = config("BEAKER_LOCAL_CACHEPATH", default="/var/www/beaker/logs")

# Location of system console logs
CONSOLE_LOGS = config("BEAKER_CONSOLE_LOGS", default="/var/consoles")

# Regex pattern to use to find panics
PANIC_REGEX = config(
    "BEAKER_PANIC_REGEX",
    default="Kernel panic|Oops[\\s:[]|general protection fault(?! ip:)|general protection handler: wrong gs|\\(XEN\\) "
            "Panic|kernel BUG at .+:[0-9]+!",
)

# Regex pattern which matches OS major names which do not support x86 EFI
EFI_EXCLUDED_OSMAJORS_REGEX = config(
    "BEAKER_EFI_EXCLUDED_OSMAJORS_REGEX",
    default="RedHatEnterpriseLinux(3|4|Server5|Client5|ServerGrid5)|Fedora1[234567]",
)
