package app;

public class C{
    public void cToB() {
        System.out.println("C::cToB");
        new B().bToA();
    }
    public void cToA() {
        System.out.println("C::cToA");
        new A().a();
    }
    public void c() {
        System.out.println("C::c");
    }
}