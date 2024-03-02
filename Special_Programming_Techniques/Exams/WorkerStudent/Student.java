public class Student implements StudentI {
    private int id;
    private String[] curricula;
    private double average;

    public Student(int id, String[] curr, double avg) {
        this.id = id;
        this.curricula = curr;
        this.average = avg;
    }

    @Override
    public int studentId() {
        return this.id;
    }

    @Override
    public String[] curricula() {
        return this.curricula;
    }

    @Override
    public double average() {
        return this.average;
    }
}