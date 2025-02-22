from threading import Thread

class NotDoneYetException(BaseException):
    def __init__(self, msg):
        self.message = msg

def asynchronous(f):
    class wrapper(Thread):
        def start(*args):
            thread = wrapper(target=f, args=args)
            super(type(thread), thread).start()
            return thread
        def run(self):
            self.result = self._target(*self._args)
        def get_result(self):
            if self.is_done():
                return self.result
            raise NotDoneYetException("the computation is not over yet")
        def is_done(self):
            return not self.is_alive()
    asynchronous.NotDoneYetException = NotDoneYetException
    return wrapper