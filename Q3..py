
from datetime import datetime
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        print(f"start: {start_time}")
        return result
    return wrapper
@timer_decorator
def decorated_function():
    print("decorated function")
decorated_function()