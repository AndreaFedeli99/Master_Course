# Let us consider a class MyMath with the following methods: fib, fact and taylor implementing the Fibonacci's series, the factorial and 
# the Taylor's series for a generic function and a level of approximation respectively. Then implement the following decorators:
# 1. @memoization applied to a method stores in the class previously calculated results and reuses them instead of recalculating
# 2. @logging applied to a method writes on a file the method name, its actual arguments when a method is called (also by recursion)
# 3. @stack_trace applied to a method prints its stack trace, i.e., the list of calls made to carry out the invocation.