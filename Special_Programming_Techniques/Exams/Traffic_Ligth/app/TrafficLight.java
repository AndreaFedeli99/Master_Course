package app;

public class TrafficLight {
    private Color state;

    public TrafficLight() { state = Color.Green; }
    public Color getState() { return state; }
    public void setState(Color c) { state = c; }
    public void go() {
        int index = state.ordinal();
        state = Color.values()[++index%3];
    }
}