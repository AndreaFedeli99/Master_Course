public class Edge {
    public Edge(String mName, Node from, Node to) {
        val = mName;
        this.from = from;
        this.to = to;
    }
    public String getVal() { return  val; }
    public Node getFrom() { return from; }
    public Node getTo() { return to; }

    @Override
    public String toString() {
        return from.toString() + " -> " + val + " -> " + to.toString();
    }

    private String val;
    private Node from;
    private Node to;
}
