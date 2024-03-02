package app;

public class CrossRoad {
    private String name;
    private TrafficLight[] trafficLights;

    public TrafficLight[] getTrafficLights() { return trafficLights; }
    
    public CrossRoad(String name, TrafficLight[] t) {
        this.name = name;
        this.trafficLights = t;
    }

    @Override
    public String toString() {
        StringBuffer sb = new StringBuffer(name + ":\t");

        for (int i = 0; i < trafficLights.length; i++)
            sb.append("TL[" + i + "]: " + trafficLights[i].getState() + "\t");

        return sb.toString();
    }

    public void go() {
        for (TrafficLight tl : trafficLights)
            tl.go();
    }
}