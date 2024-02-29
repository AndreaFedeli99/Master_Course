import java.io.FileInputStream;

public class CounterClassLoader extends ClassLoader {
    public CounterClassLoader (ClassLoader parent) {
        super(parent);
    }
    @Override
    public Class<?> loadClass(String name) throws ClassNotFoundException {
        System.out.println("I'm loading " + name);
        if (!name.startsWith("java.")) {
            localCount++;
            return this.findClass(name);
        }
        else {
            javaCount++;
            return super.loadClass(name);
        }
    }

    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {
        String clsPath = name.replace(".", "\\") + ".class";
        try {
            FileInputStream fs = new FileInputStream(clsPath);
            byte[] b = fs.readAllBytes();
            return defineClass(name, b, 0, b.length);
        }
        catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public static void printCounters() {
        System.out.println("ClassLoader loaded " + localCount + " local classes and " + javaCount + " java classes");
    }
    private static int localCount = 0;
    private static int javaCount = 0;
}
