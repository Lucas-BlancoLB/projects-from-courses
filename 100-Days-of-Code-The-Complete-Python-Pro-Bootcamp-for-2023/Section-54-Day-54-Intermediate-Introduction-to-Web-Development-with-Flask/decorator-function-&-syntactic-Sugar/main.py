import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(funct):
    def wrapper():
        past_time = time.time()
        funct()
        delta_time = time.time() - past_time
        print(f"{funct.__name__} run speed: {delta_time}s")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
