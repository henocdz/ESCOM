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


        Figura triangulo = new Figura(new Punto(2,3),new Punto(1,0),new Punto(3,0));
        
        Figura cuadrado = new Figura(new Punto(0,0),new Punto(2,2));
        
        Figura circulo = new Figura(new Punto(5,5));
        
        System.out.print("\nTriangulo 1 \n\tArea:"+triangulo.calcularArea() +"\n\tPerimetro F1: " + triangulo.calcularPerimetro() + "\n\n ----------------- \n");
        
        System.out.print("\nCuadrado 1 \n\tArea:"+cuadrado.calcularArea() +"\n\tPerimetro F1: " + cuadrado.calcularPerimetro() + "\n\n ----------------- \n");
        
        System.out.print("\n Circulo 1 \n\tArea:"+circulo.calcularArea(3) +"\n\tPerimetro F1: " + circulo.calcularPerimetro(3) + "\n\n ----------------- \n");
    }
}
