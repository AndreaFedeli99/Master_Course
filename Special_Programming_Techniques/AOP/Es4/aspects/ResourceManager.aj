package aspects;

import app.Resource;

import java.util.HashMap;
import java.util.Vector;

public aspect ResourceManager implements ResourcePool {
    private HashMap<String, Vector<Resource>> pool = new HashMap<String, Vector<Resource>>();

    public Resource getResource(String type) {
        try {
            return pool.get(type).get(0);
        }
        catch(NullPointerException | ArrayIndexOutOfBoundsException exc) {
            return null;
        }
    }

    public void releaseResource(String type, Resource r) {
        if (pool.containsKey(type))
            pool.get(type).add(r);
        else {
            Vector<Resource> resources = new Vector<Resource>();
            resources.add(r);
            pool.put(type, resources);
        }
    }

    pointcut resourcesCreation() : execution(app.Resource+.new(..)) && !within(app.Resource);
    pointcut resourcesDestruction(Resource r) : call(void app.Resource+.destroy()) && target(r);

    Object around() : resourcesCreation() {
        String type = thisJoinPointStaticPart.getSignature().getDeclaringTypeName();
        Resource rObj = getResource(type);
        if (rObj != null) {
            System.out.println("*** I'm pooling an " + type + " instance");
            return rObj;
        }
        else
            return proceed();
    }

    before(Resource r) : resourcesDestruction(r) {
        System.out.println("*** I'm storing an " + r.getClass().getName() + " instance");
        releaseResource(r.getClass().getName(), r);
    }
}