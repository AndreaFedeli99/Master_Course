package app;

public class Main {
    public static void main(String[] args) {
        CrossRoad cr1 = new CrossRoad("Cr1", new TrafficLight[] {
            new TrafficLight(), new TrafficLight(), new TrafficLight()
        });
        CrossRoad cr2 = new CrossRoad("Cr2", new TrafficLight[] {
            new TrafficLight(), new TrafficLight(), new TrafficLight(), new TrafficLight()
        });

        for (int i=0; i < 10; i++) {
            System.out.println(cr1);
            System.out.println(cr2);

            cr1.go();
            cr2.go();
        }
    }
}