from threading import Thread

class NotYetDoneException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.message = msg

class WrapperThread(Thread):
    def __init__(self, target, args, *other):
        self.t = target
        super().__init__(target=self.target, args=args, *other)

    def target(self, *args):
        self.result = self.t(*args)

    def is_done(self):
        return not self.is_alive()
    
    def get_result(self):
        if self.is_done():
            return self.result
        raise NotYetDoneException('the call has not yet completed its task')

def asynchronous(f):
    class Wrapper:
        def start(self, *args):
            thread = WrapperThread(target=f, args=args)
            thread.start()
            return thread
        
        def __call__(self, *args):
            return f(*args)
        
    return Wrapper()

asynchronous.NotYetDoneException = NotYetDoneException