
from datetime import datetime
import random
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        try:
            result = func(*args, **kwargs)
        except Exception:
            print("Error in running the function.")
            result = None
        print(f"start: {start_time}")
        return result
    return wrapper

@timer_decorator
def simulate_weather(days, start_temp = 25):
    if not isinstance(days, int) or days < 0:
        print("Invalid input")
        return []
    temps = [start_temp]
    for i in range(1, days):
        change = random.randint(-2, 3)
        temps.append(temps[-1] + change)
    return temps
result = simulate_weather(10)
print(result)
