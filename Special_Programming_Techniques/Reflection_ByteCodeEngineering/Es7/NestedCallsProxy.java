import java.lang.invoke.MethodHandle;
import java.lang.invoke.MethodHandles;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.util.Arrays;

public class NestedCallsProxy extends NestedCalls implements InvocationHandler {
    public NestedCallsProxy() {
        proxy = (NestedCallsI) Proxy.newProxyInstance(
                this.getClass().getClassLoader(),
                new Class[] { NestedCallsI.class },
                this
        );
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        Object res;
        Method superMethod = NestedCalls.class.getMethod(
                method.getName(),
                method.getParameterTypes()
        );
        System.out.println("*".repeat(++lvl));
        MethodHandle mh = MethodHandles.lookup().unreflectSpecial(superMethod, this.getClass());
        res = mh.bindTo(this).invokeWithArguments(args);
        System.out.println("*".repeat(--lvl));
        return res;
    }

    @Override
    public int a() { return proxy.a(); }
    @Override
    public int b(int a) { return proxy.b(a); }
    @Override
    public int c(int a) { return proxy.c(a); }

    private final NestedCallsI proxy;
    private int lvl = 0;
}
