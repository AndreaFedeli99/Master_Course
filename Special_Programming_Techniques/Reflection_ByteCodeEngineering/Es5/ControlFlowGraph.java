import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.Map;
import java.util.Optional;

public class ControlFlowGraph {

    public ControlFlowGraph(String[] clsNames) {
        Class<?>[] classes = Arrays.stream(clsNames)
                .map(ControlFlowGraph::getClass)
                .filter(Optional::isPresent)
                .map(Optional::get)
                .toArray(Class[]::new);

        
    }

    @Override
    public String toString() {
        // return root.toString();
        return null;
    }

    public static void main(String[] args) {
        ControlFlowGraph cfg = new ControlFlowGraph(args);
    }

    private static Optional<Class<?>> getClass(String clsName) {
        try {
            return Optional.of(loader.loadClass(clsName));
        }
        catch(ClassNotFoundException e){
            return Optional.empty();
        }
    }
    private Method[] getAnnotatedMethod(Class<?> cls) {
        return Arrays.stream(cls.getDeclaredMethods())
                .filter(m -> m.getAnnotation(ControlFlow.class) != null)
                .toArray(Method[]::new);
    }
    private Node buildTree(Node r) {

    }

    private Node root;
    private Map<Node, Edge[]> data;
    private static final GraphAnnotationClassLoader loader = new GraphAnnotationClassLoader();

}
