import java.lang.reflect.Member;
import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.Map;
import java.util.Optional;

public class ElementRecognizer {
    public static void main(String[] args) {
        String[] classes = { "ElementRecognizer", "java.lang.String" };
        String[] members = { "main", "init", "isInMembers", "classMembers", "toString" };

        ElementRecognizer.init(classes, members);

        System.out.println("There is a class that contains all the specified members: " + ElementRecognizer.checkAllContained(members) + "\n");

        ElementRecognizer.classMembers.forEach((cls, tMembers) -> {
            for (Member member : tMembers) {
                System.out.println("The member " + member.getName() + " is declared in " + cls.getName());
                System.out.println("It's a " + (member instanceof Method ? "method " : "field"));
                System.out.println("Signature: " + member);
                System.out.println();
            }
        });
    }

    public static void init(String[] classes, String[] members) {
        Class<?>[] tClasses;
        Map.Entry<Class<?>, Member[]>[] entries;

        tClasses = Arrays.stream(classes)
                    .map(clsName -> {
                        try {
                            return Optional.of(Class.forName(clsName));
                        }
                        catch (ClassNotFoundException e) {
                            return Optional.empty();
                        }
                    })
                    .filter(Optional::isPresent)
                    .map(Optional::get)
                    .toArray(Class[]::new);

        entries = Arrays.stream(tClasses)
                        .map(cls ->
                            Map.entry(
                                cls,
                                Arrays.stream(members)
                                    .map(memberName -> {
                                        Optional<Member> tMember;
                                        tMember = isInMembers(cls.getDeclaredMethods(), memberName);
                                        if (tMember.isEmpty())
                                            tMember = isInMembers(cls.getDeclaredFields(), memberName);
                                        return tMember;
                                    })
                                    .filter(Optional::isPresent)
                                    .map(Optional::get)
                                    .toArray(Member[]::new)
                            )
                        )
                        .toArray(Map.Entry[]::new);

        ElementRecognizer.classMembers = Map.ofEntries(entries);
    }

    private static boolean checkAllContained(String[] members) {
        return ElementRecognizer.classMembers.entrySet().stream().anyMatch(entry -> entry.getValue().length == members.length);
    }

    private static Optional<Member> isInMembers(Member[] members, String memberName) {
        return Arrays.stream(members).filter(method -> method.getName().equals(memberName)).findFirst();
    }

    private static Map<Class<?>, Member[]> classMembers;
}
