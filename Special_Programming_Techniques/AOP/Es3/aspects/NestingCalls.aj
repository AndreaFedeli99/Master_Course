package aspects;

public aspect NestingCalls {
    pointcut targetCalls(int b) : call(int app.*.*(..)) && args(b);

    int around(int b) : targetCalls(b) {
        return proceed(proceed(b));
    }
}