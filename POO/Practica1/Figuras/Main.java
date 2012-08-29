class Main {
    public static void main(String args[])
    {
        //Triangulos
        Triangulo t = new Triangulo();
        Triangulo t2 = new Triangulo(2.0,1.0,3.0);
        Triangulo t3 = new Triangulo(t2);

        //Cuadrados
        Cuadrado c = new Cuadrado();
        Cuadrado c2 = new Cuadrado(5.0);
        Cuadrado c3 = new Cuadrado(c2);

        //Circulos
        Circulo q = new Circulo();
        Circulo q2 = new Circulo(3.2);
        Circulo q3 = new Circulo(q2);
        
        System.out.println("-> Triangulo 1");
        System.out.println("\t Area: " + t.getArea());
        System.out.println("\t Perimetro: " + t.getPerimetro());
        System.out.println("-> Triangulo 2");
        System.out.println("\t Area: " + t2.getArea());
        System.out.println("\t Perimetro: " + t2.getPerimetro());
        System.out.println("-> Triangulo 3");
        System.out.println("\t Area: " + t3.getArea());
        System.out.println("\t Perimetro: " + t3.getPerimetro());
        
        System.out.println("===============================");
        System.out.println("-> Cuadrado 1");
        System.out.println("\t Area: " + c.getArea());
        System.out.println("\t Perimetro: " + c.getPerimetro());
        System.out.println("-> Cuadrado 2");
        System.out.println("\t Area: " + c2.getArea());
        System.out.println("\t Perimetro: " + c2.getPerimetro());
        System.out.println("-> Cuadrado 3");
        System.out.println("\t Area: " + c3.getArea());
        System.out.println("\t Perimetro: " + c3.getPerimetro());
        
        System.out.println("===============================");
        System.out.println("-> Circulo 1");
        System.out.println("\t Area: " + q.getArea());
        System.out.println("\t Perimetro: " + q.getPerimetro());
        
        System.out.println("-> Circulo 2");
        System.out.println("\t Area: " + q2.getArea());
        System.out.println("\t Perimetro: " + q2.getPerimetro());
        System.out.println("-> Circulo 3");
        System.out.println("\t Area: " + q3.getArea());
        System.out.println("\t Perimetro: " + q3.getPerimetro());
    }
}
