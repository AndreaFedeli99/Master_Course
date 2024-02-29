package app;

public class A {
    public void a() {
        System.out.println("A::a");
    }
    public void aToC() {
        System.out.println("A::aToC");
        new C().c();
    }
}