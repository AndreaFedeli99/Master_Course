package app;

public class Main {
    public static void main(String[] args) {
        System.out.println("B -> C -> A");
        new B().bToC();

        System.out.println("\nC -> B -> A");
        new C().cToB();

        System.out.println("\nD -> B -> A");
        new D().dToB();

        System.out.println("\nD -> C -> B -> A")
        new D().dToCToB();

        System.out.println("\nB -> A -> C")
        new B().bToA();

        System.out.println("\nD -> B -> C -> A")
        new D().dToBToC();
    }
}