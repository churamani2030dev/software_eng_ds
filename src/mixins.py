class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
