import java.lang.reflect.Proxy;

public class MainNestedCalls {
    public static void main(String[] args) {
        NestedCalls nc = new NestedCallsProxy();

        System.out.println("a() :- " + nc.a());
        System.out.println("b(a()) :- " + nc.b(nc.a()));
        System.out.println("c(b(a)) :- " + nc.c(nc.b(nc.a())));
    }
}
