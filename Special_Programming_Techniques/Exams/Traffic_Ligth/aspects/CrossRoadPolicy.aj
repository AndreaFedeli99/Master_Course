package aspects;

import app.Color;
import app.CrossRoad;
import app.TrafficLight;

public aspect CrossRoadPolicy {
    pointcut crCreation(CrossRoad cr) : execution(app.CrossRoad.new(..)) && target(cr);
    pointcut crGo(CrossRoad cr) : call(* app.CrossRoad.go()) && target(cr);

    after(CrossRoad cr) : crCreation(cr) {
        TrafficLight[] tl = cr.getTrafficLights();
        for (int i = 0; i < tl.length; i++)
            tl[i].setState(i % 2 == 0 ? Color.Green : Color.Red);
    }

    after(CrossRoad cr) : crGo(cr) {
        TrafficLight[] tl = cr.getTrafficLights();
        if (tl[0].getState() == Color.Yellow || tl[1].getState() == Color.Yellow) {
            for (TrafficLight t : tl) {
                if (t.getState() == Color.Green)
                    t.setState(Color.Red);
            }
        }
    }
}