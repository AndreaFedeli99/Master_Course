import java.lang.reflect.*;

public class WorkerStudentFactory {
    public static WorkerStudent getInstance(int studentId, String[] curr, double avg, int workerId, double salary) {
        Handler h = new Handler(new Student(studentId, curr, avg), new Worker(workerId, salary));
        return (WorkerStudent) Proxy.newProxyInstance(h.getClass().getClassLoader(), new Class[] { WorkerStudent.class }, h);
    }

    public static WorkerStudent getInstance(Student s, Worker w) {
        Handler h = new Handler(s, w);
        return (WorkerStudent) Proxy.newProxyInstance(h.getClass().getClassLoader(), new Class[] { WorkerStudent.class }, h);
    }
}