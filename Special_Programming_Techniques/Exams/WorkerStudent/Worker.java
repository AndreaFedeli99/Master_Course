public class Worker implements WorkerI {
    private int id;
    private double monthSalary;
    private double yearSalary;

    public Worker(int id, double salary) {
        this.id = id;
        this.monthSalary = salary;
        this.yearSalary = salary * 12;
    }

    @Override
    public int workerId() {
        return this.id;
    }

    @Override
    public double monthSalary() {
        return this.monthSalary;
    }

    @Override
    public double yearSalary() {
        return this.yearSalary;
    }
}