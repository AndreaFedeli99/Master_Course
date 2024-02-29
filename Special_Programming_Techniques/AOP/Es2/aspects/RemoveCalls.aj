package aspects;

public aspect RemoveCalls {
    pointcut targetCalls() :
        call(* app.A.*(..))
        &&
        (
            this(app.B)
            ||
            (
                cflow(call(* app.B.*(..)))
                &&
                !cflow(call(* app.C.*(..)))
            )
        );
    
    void around() : targetCalls() {
        System.out.println("removeAspect :- call to A removed");
    }
}