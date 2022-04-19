import java.util.Scanner;

public class Main {
    public static void main(String[] args)  {
        Tabela t = new Tabela();
        Scanner keyboard = new Scanner(System.in);
        int i = 0;

        System.out.println("SETTING VARIABLE NAMES");
        System.out.print("Insert var1: ");
        String v1 = keyboard.nextLine();
        System.out.print("Insert var2: ");
        String v2 = keyboard.nextLine();
        System.out.printf("%10s", v1);
        System.out.printf("%10s", v2);
        System.out.printf("%10s", "¬" + v1);
        System.out.printf("%10s", "¬" + v2);
        System.out.printf("%15s", v1 + " ^ " + v2);
        System.out.printf("%10s", v1 + " v " + v2);
        System.out.printf("%10s", v1 + " -> " + v2);
        System.out.printf("%10s", v1 + " <-> " + v2);
        System.out.println();

        do {
            if (i == 0) {
                t.var1 = false;
                t.var2 = false;
                i++;
            } else if (i == 1) {
                t.var1 = false;
                t.var2 = true;
                i++;
            } else if (i == 2) {
                t.var1 = true;
                t.var2 = false;
                i++;
            } else if (i == 3){
                t.var1 = true;
                t.var2 = true;
                i++;
            }
            System.out.printf("%10s ", t.var1);
            System.out.printf("%10s ", t.var2);
            System.out.printf("%10s ", t.negation1());
            System.out.printf("%10s ", t.negation2());
            System.out.printf("%10s", t.conjunction());
            System.out.printf("%10s", t.disjunct() );
            System.out.printf("%10s", t.implication());
            System.out.printf("%10s", t.biconditional());
            System.out.println();
        } while (i < 4);
    }
}

