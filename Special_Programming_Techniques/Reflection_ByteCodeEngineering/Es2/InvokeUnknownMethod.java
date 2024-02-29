import java.lang.reflect.*;
import java.util.Arrays;
import java.util.regex.Pattern;

public class InvokeUnknownMethod {
    public static void main(String[] args) {
        if (args.length < 2)
            System.out.println("Please use args to specify the class, method and method's parameters to be called...");
        else{
            try {
                Class<?> cls = Class.forName(args[0]);
                String[] arguments = Arrays.copyOfRange(args, 2, args.length);

                Class<?>[] argTypes = InvokeUnknownMethod.getArgsTypes(arguments);
                Method m = cls.getMethod(args[1], argTypes);

                Object inst = cls.getDeclaredConstructor().newInstance();
                Object res = m.invoke(inst, getArgsValue(arguments, argTypes));
                System.out.println(res);
            }
            catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    public static Class<?>[] getArgsTypes(String[] args) {
        Class<?>[] types = new Class[args.length];

        for (int i = 0; i < args.length; i++) {
            if (Pattern.matches("^[+-]?\\d+.\\d+", args[i]))
                types[i] = double.class;
            else
                types[i] = int.class;
        }

        return types;
    }

    public static Object[] getArgsValue(String[] values, Class<?>[] types) {
        Object[] argValues = new Object[values.length];

        for (int i = 0; i < values.length; i++) {
            if (types[i].equals(double.class))
                argValues[i] = Double.valueOf(values[i]);
            else
                argValues[i] = Integer.valueOf(values[i]);
        }

        return argValues;
    }
}
