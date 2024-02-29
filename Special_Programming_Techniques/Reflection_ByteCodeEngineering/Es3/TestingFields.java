import java.lang.reflect.Array;
import java.lang.reflect.Field;
import java.util.Arrays;
import java.util.Date;
import java.util.stream.Collectors;

public class TestingFields {
    private Double d[];
    private Date dd;
    public static final int i = 42;
    protected static String s = "testing ...";

    public TestingFields(int n, double val) {
        dd = new Date();
        d = new Double[n];
        for (int i=0; i<n; i++) d[i] = i*val;
    }

    public static void main(String[] args) {
        TestingFields tf = new TestingFields(7, 3.14);
        TestingFields tf2 = new TestingFields(5, 1);
        TestingFields.showState(tf);
        TestingFields.showState(tf2);

        System.out.println("\nChanging static field value...\n");

        TestingFields.updateField(tf, "s", "testing ... passed!!!");
        TestingFields.showState(tf);
        TestingFields.showState(tf2);
    }

    public static void showState(Object obj) {
        Class<?> cls = obj.getClass();

        System.out.println("----------------------------------------");
        System.out.println("State of " + cls.getName() + " instance\n");

        Arrays.stream(obj.getClass().getDeclaredFields()).forEach(field -> {
            try {
                if (field.getType().isArray())
                    System.out.println(
                        field.getType().getComponentType() + "[] "
                        + field.getName() + " = ["
                        + (field.get(obj) != null ?
                            Arrays.stream((Object[])field.get(obj)).map(Object::toString).collect(Collectors.joining(", "))
                            :
                            ""
                        )
                        + "]"
                    );
                else
                    System.out.println(
                         field.getType() + " "
                         + field.getName() + " = "
                         + field.get(obj)
                    );
            }
            catch (Exception e) {
                e.printStackTrace();
            }
        });
        System.out.println("----------------------------------------");
    }

    public static void updateField(Object obj, String fieldName, Object val) {
        try {
            Field f = obj.getClass().getDeclaredField(fieldName);
            f.set(obj, val);
        }
        catch (Exception e) {
            System.out.println("Field not found...");
        }
    }
}
