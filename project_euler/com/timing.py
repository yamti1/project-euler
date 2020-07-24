from decorator import decorator
from datetime import datetime


@decorator
def timed(func, *args, **kwargs):
    start = datetime.now()
    try:
        result = func(*args, **kwargs)
        return result
    finally:
        end = datetime.now()
        print(f"{func.__name__} took {(end - start).total_seconds()}s")
