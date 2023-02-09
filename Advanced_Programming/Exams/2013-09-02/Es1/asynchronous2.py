# To run this version you have to remove "asynchronous" before "NotYetDoneException" in Es1.py

from threading import Thread

class NotYetDoneException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.message = msg

def asynchronous(f):
    class Wrapper:
        def start(self, *args, **kwargs):
            class Result:
                def target(self, *args):
                    self.result = f(*args)
                def is_done(self):
                    return not thread.is_alive()
                def get_result(self):
                    if not self.is_done():
                        raise NotYetDoneException('the call has not yet completed its task')
                    else:
                        return self.result
            res = Result()
            thread = Thread(target=res.target, args=args, kwargs=kwargs)
            thread.start()
            return res
        
        def __call__(self, *args):
            return f(*args)
        
    return Wrapper()