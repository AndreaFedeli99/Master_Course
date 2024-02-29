import java.util.ArrayList;

public class ClassLoaderMain {
    public static void main(String[] args) {
        double n = 3.14;

        String s = "abcd";

        ArrayList<Integer> l = new ArrayList<>();

        StringBuilder sb = new StringBuilder();

        CounterClassLoader.printCounters();
    }
}
