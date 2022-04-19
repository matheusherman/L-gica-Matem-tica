public class Tabela {

    boolean var1, var2;


    public boolean negation1() {
        if (var1 == true) {
            return false;
        } else {
            return true;
        }
    }

    public boolean negation2() {
        if (var2 == true) {
            return false;
        } else {
            return true;
        }
    }

    public boolean conjunction() {
        if (var1 && var2 == true) {
            return true;
        } else {
            return false;
        }
    }
    public boolean disjunct() {
        if (var1 && var2 == false) {
            return false;
        } else {
            return true;
        }
    }
        public boolean implication() {
            if (var1 == true && var2 == false) {
                return false;
            } else {
                return true;
            }
        }
        public boolean biconditional() {
            if (var1 == var2) {
                return true;
            } else {
                return false;
            }
    }
}

