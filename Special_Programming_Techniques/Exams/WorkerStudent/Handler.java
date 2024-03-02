import java.lang.reflect.*;
import java.util.*;

public class Handler implements InvocationHandler {
    private StudentI student;
    private WorkerI worker;

    public Handler(StudentI s, WorkerI w) {
        this.student = s;
        this.worker = w;
    }

    private boolean methodEqual(Method m1, Method m2) {
        return m1.getName().equals(m2.getName()) && Arrays.equals(m1.getParametersType(), m2.getParametersType()) && m1.getReturnType().equals(m2.getReturnType());
    }

    private boolean isClassMethod(Class cls, Method method) {
        return Arrays.stream(cls.getMethods()).anyMatch(m -> methodEqual(method, m));
    }

    private Object invoke(Object p, Method m, Object[] args) throws NotSuchMethodException, IllegalAccessException, InvocationTargetException{
        if (isClassMethod(student.getClass(), m)) {
            return m.invoke(student, args);
        }
        if (isClassMethod(worker.getClass(), m)) {
            return m.invoke(worker, args);
        }
        throw new NotSuchMethodException("The method doesn't belong neither to Student or Worker");
    }
}