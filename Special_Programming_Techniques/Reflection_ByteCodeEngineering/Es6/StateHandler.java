import java.lang.reflect.*;
import java.util.Arrays;
import java.util.Objects;
import java.util.stream.Collectors;

public class StateHandler implements InvocationHandler {

    public static void main(String[] args) {
        ITestingFields tf = (ITestingFields) Proxy.newProxyInstance(TestingFields.class.getClassLoader(), TestingFields.class.getInterfaces(), new StateHandler(new TestingFields(7, 3.14)));
        tf.setAnswer(15);
        tf.message();
    }

    public StateHandler(Object base) { baseObj = base; }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("--------------------------------------------------");
        System.out.println(":- calling " + method.getName());
        showStatus();
        System.out.println("--------------------------------------------------");
        Object res = method.invoke(baseObj, args);
        System.out.println("--------------------------------------------------");
        System.out.println(":- called " + method.getName());
        showStatus();
        System.out.println("--------------------------------------------------");
        return res;
    }

    private void showStatus() {
        for (Field f : baseObj.getClass().getDeclaredFields()) {
            f.setAccessible(true);
            try {
                if (f.getType().isArray()) {
                    System.out.println(f.getName() + " = [" + Arrays.stream((Object[])f.get(baseObj)).map(Object::toString).collect(Collectors.joining(", ")) + "]");
                } else {
                    System.out.println(f.getName() + " = " + f.get(baseObj));
                }
            }
            catch (Exception e) { e.printStackTrace(); }
        }
    }

    private Object baseObj;
}
