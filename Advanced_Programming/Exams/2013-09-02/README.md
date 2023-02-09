# Exam of Advanced Programming

###### 2013-09-02

## Exercise 1

Implement a **decorator** that once applied to a function each call to such a function is done asynchronously, i.e., a separate thread takes care of its execution and the main thread goes on with the rest of the execution. Note that the two threads need to be synchronized on the result of the computation: this is necessary in the main thread but not immediately available.

The solution have to be composed by a class (called `Future` in the literature) wrapping the return value that provides a method, called `get_result`, to get the result if available (if the result is not available yet and you try to access to it, it raises an exception that needs to be called `NotYetDoneException`). Also it must provide a method `is_done` to test if the return value has been calculated or not. Any asynchronous computation is separated.

**Hint**: You have to use the standard module `threading`

### Test example:

```py
from asynchronous import *

if __name__ == "__main__":
    import time

    @asynchronous
    def long_process(num):
        time.sleep(10)
        return num * num

    result = long_process.start(12)
    
    for i in range(20):
        time.sleep(1)
        
        if result.is_done():
            print("[{1}]: result {0}".format(result.get_result(), i))
        else: print("[{0}]: not ready yet".format(i))

    result2 = long_process.start(13)

    try:
        print("result2 {0}".format(result2.get_result()))
    except asynchronous.NotYetDoneException as ex:
        print(ex.message)
```

### Expected output:

```code
[0]: not ready yet
[1]: not ready yet
[2]: not ready yet
[3]: not ready yet
[4]: not ready yet
[5]: not ready yet
[6]: not ready yet
[7]: not ready yet
[8]: not ready yet
[9]: result 144
[10]: result 144
[11]: result 144
[12]: result 144
[13]: result 144
[14]: result 144
[15]: result 144
[16]: result 144
[17]: result 144
[18]: result 144
[19]: result 144
the call has not yet completed its task
```

## Exercise 2

Implement the following **generators** to wrap other generators:

- `even(s)`: this returns the even elements of the generator `s` at each iteration
- `stopAt(s, n)`: this generator stops iterate when the next element of `s` is greater than `n`; it only works for sorted generators
- `buffer(s, n)`: this generator at each iteration returns a chunk of `n` consecutive elements of the generator `s`; note that last chunk can be shorter
- `conditional(s, p)`: this generator returns each generator's element (`s`) whose **successive** element respects the predicate `p`

### Test example:

```py
from generators import *

def fib():
    x,y = 1,1
    while True:
        yield x
        x,y = y, x+y

if __name__ == "__main__":
    even_fib = even(fib())
    for i in range(10): print(next(even_fib), end=' ')
    print()

    for i in stopAt(even(fib()), 40000000): print(i, end=' ')
    print()

    buffered_limited_fib = buffer(stopAt(fib(),3000), 5)
    for i in buffered_limited_fib: print(i)
    
    condfib = conditional(fib(), lambda x: (x%2 == 0))
    for i in range(10): print(next(condfib), end=' ')
    print()

    condfib2 = conditional(fib(), lambda x: (x%2 != 0))
    for i in range(15): print(next(condfib2), end=' ')
    print()
```

### Expected output:

```code
2 8 34 144 610 2584 10946 46368 196418 832040
2 8 34 144 610 2584 10946 46368 196418 832040 3524578 14930352
[1, 1, 2, 3, 5]
[8, 13, 21, 34, 55]
[89, 144, 233, 377, 610]
[987, 1597, 2584]
1 5 21 89 377 1597 6765 28657 121393 514229
1 2 3 8 13 34 55 144 233 610 987 2584 4181 10946 17711
```