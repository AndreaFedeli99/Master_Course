import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
public @interface InvokedMethod {
    Class<?> cls();
    String name();
}
