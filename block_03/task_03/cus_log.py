from typing import Callable, Any
from datetime import datetime as dt
from functools import wraps

_LOGFILE = 'debug_log.txt'

__all__ = [
    'log_deco',
]


def log_deco(func: Callable) -> Callable:
    """ Just a logger to monitor a caching class for decorator """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        with open(_LOGFILE, 'a', encoding='utf-8') as f_out:
            args_line = (' '.join([f'type: {type(pos)}' for pos in args])
                         if args else 'empty args')
            kwargs_line = (' '.join([f'type: {type(pos)}' for pos in args])
                           if kwargs else None)
            log_string = (f'{dt.now().strftime("%Y-%m-%d@%H:%M:%S"):25}'
                          f'FUNC: {func.__name__}\nARGS: {args_line}\n')
            if kwargs_line:
                log_string += f'KWARGS: {kwargs_line}\n'
            try:
                result = func(*args)
                log_string += f'RESULT at {dt.now().strftime("%Y-%m-%d@%H:%M:%S")}: type: {type(result)}'
            except Exception as exc:
                log_string += f'EXCEPTION: {exc}'
                raise exc
            finally:
                f_out.write(log_string + '\n\n')
            return result

    return wrapper
