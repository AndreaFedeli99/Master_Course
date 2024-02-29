public class Node {
    public Node(Class<?> cls) {
        val = cls;
    }
    public Class<?> getVal() { return val; }

    @Override
    public String toString() {
        return " { " + val.getName() + " } ";
    }

    private Class<?> val;
}
