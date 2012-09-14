package Figuras;

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Roofdier
 */
public class Main {
    public static void main(String args[])
    {
        Punto p1,p2,p3;
    
        p1 = new Punto(2,3);
        p2 = new Punto(1,0);
        p3 = new Punto(3,0);
        
        Figura fig1 = new Figura(p1,p2,p3);
        
        System.out.print("\nFigura 1 \n\tArea:"+fig1.calcularArea() +"\n\tPerimetro F1: " + fig1.calcularPerimetro() + "\n\n ----------------- \n");
    }
}
