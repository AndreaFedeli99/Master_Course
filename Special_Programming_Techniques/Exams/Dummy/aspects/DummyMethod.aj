package aspects;

import java.util.HashMap;
import org.aspectj.lang.reflect.MethodSignature;

public aspect DummyMethod pertarget(targetCalls()) {
    private HashMap<String, Object[]> methodsMap = new HashMap<String, Object[]>();

    private Object getCurrentArgs(Object newArg, Object oldArg) {
        Class<?> cls = oldArg.getClass();
        if (cls.equals(Integer.class))
            return (int)oldArg + (int)newArg;
        if (cls.equals(String.class))
            return (String)oldArg + (String)newArg;
        return null;
    }

    pointcut targetCalls() : call(* *.*(..)) && !within(aspects..*) && !call(* java..*(..));

    void around() : targetCalls() {
        String signature = thisJoinPointStaticPart.getSignature().toString();

        if (methodsMap.containsKey(signature)) {
            Object[] oldArgs = methodsMap.get(signature);
            Object[] newArgs = thisJoinPoint.getArgs();

            for (int i = 0; i < newArgs.length; i++) {
                newArgs[i] = getCurrentArgs(newArgs[i], oldArgs[i]);
            }

            methodsMap.remove(signature);

            try {
                ((MethodSignature)thisJoinPoint.getSignature()).getMethod().invoke(thisJoinPoint.getTarget(), newArgs);
            }
            catch(Exception exc) { exc.printStackTrace(); }
        }
        else {
            methodsMap.put(signature, thisJoinPoint.getArgs());
        }
    }
}