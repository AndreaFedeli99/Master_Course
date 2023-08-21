def multi_triggered(count, func):
    def wrapper(f):
        calls = 0
        prev_args = ()
        def inner(*args, **kwargs):
            nonlocal calls, prev_args
            calls += 1
            if calls == count:
                calls = 0
                res = f(args[0], *(func(prev_args[i-1], args[i]) for i in range(1, len(args))), **kwargs)
                prev_args = ()
                return res
            else:
                if len(prev_args) == len(args) - 1:
                    prev_args = tuple(func(prev_args[i-1], args[i]) for i in range(1, len(args)))
                else:
                    prev_args = tuple(args[i] for i in range(1, len(args)))
        return inner
    return wrapper