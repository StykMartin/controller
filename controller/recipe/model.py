from pydantic import BaseModel


class WatchdogRead(BaseModel):
    seconds: int
