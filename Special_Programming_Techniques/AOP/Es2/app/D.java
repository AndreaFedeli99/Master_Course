package app;

public class D {
    public void dToA() {
        System.out.println("D::dToA");
        new A().a();
    }
    public void dToB() {
        System.out.println("D::dToB");
        new B().bToA();
    }
    public void dToC() {
        System.out.println("D::dToC");
        new C().c();
    }
    public void dToCToB() {
        System.out.println("D::dToCToB");
        new C().cToB();
    }
    public void dToBToC() {
        System.out.println("D::dToBToC");
        new B().bToC();
    }
}