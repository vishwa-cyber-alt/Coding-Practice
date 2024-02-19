class Poly {
    public void one() {
        System.out.print("its one");
    }
}

class First extends Poly {
    public void first() {
        System.out.print("its first");
    }
}

class Second extends Poly {
    public void two() {
        System.out.print("its second");
    }
}

class Main {
    public static void main(String args[]) {
        Poly ob = new First();
        Second obj = new Second(); 
        ob.one();
        obj.two(); 
    }
}
