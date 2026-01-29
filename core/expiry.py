import time


def is_expired(created_time: float, expiry_seconds: int) -> bool:
    return (time.time() - created_time) > expiry_seconds
