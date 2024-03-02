package app;

public class Main {
    public static void main(String[] args) {
        Dummy d1 = new Dummy();
        Dummy d2 = new Dummy();

        d1.m1("A");
        d2.m1("B");
        d2.m1("C");

        d2.m2(1);
        d2.m2("A", 1);

        d1.m2(1);
        d1.m2("A", 1);

        d2.m2(1);
        d2.m2("A", 1);

        d1.m1("B");
        d1.m2("B", 1);
    }
}