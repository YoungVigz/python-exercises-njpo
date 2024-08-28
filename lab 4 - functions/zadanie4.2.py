from functools import wraps

def limit_arguments(min_value, max_value):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def clamp(value):
                if isinstance(value, (int, float)):
                    return max(min(value, max_value), min_value)
                elif isinstance(value, (list, tuple, set)):
                    return type(value)(clamp(x) for x in value)
                elif isinstance(value, dict):
                    return {k: clamp(v) for k, v in value.items()}
                # Strings and other unsupported types remain unchanged
                return value

            # Apply clamping only to the first argument, if it's numeric or iterable
            new_args = (clamp(args[0]), *args[1:]) if args else args

            return func(*new_args, **kwargs)
        
        return wrapper
    return decorator
