package app;

public class B {
    public void bToA() {
        System.out.println("B::bToA");
        new A().a();
    }
    public void bToC() {
        System.out.println("B::bToC");
        new C().c();
    }
}