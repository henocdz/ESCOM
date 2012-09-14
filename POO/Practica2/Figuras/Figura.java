package Figuras;

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Roofdier
 */
import java.util.ArrayList;

public class Figura {
    private String nombre;
    private double area;
    private double perimetro;
    private ArrayList <Punto> coords;
    
    private String type;
    
    public Figura(Punto p1)
    {
        this.nombre = "Circulo";
        this.coords = new ArrayList <Punto> ();
        this.coords.add(p1);
    }
    
    public Figura(Punto p1,Punto p2)
    {
        this.nombre = "Cuadrado";
        this.coords = new ArrayList <Punto> ();
        this.coords.add(p1);
        this.coords.add(p2);
    }
    
    public Figura(Punto p1, Punto p2, Punto p3)
    {
        this.nombre = "Triangulo";
        this.coords = new ArrayList <Punto> ();
        this.coords.add(p1);
        this.coords.add(p2);
        this.coords.add(p3);
    }
    
    
    public double calcularArea(double r)
    {
        return Math.PI * Math.pow(r,2);
    }
    
    public double calcularPerimetro(double r)
    {
        return Math.PI * (r*2);
    }
    
    public double calcularArea()
    {
        if((this.nombre).equals("Cuadrado"))
        {
            double w,h,x1,x2,y1,y2;
            x1 = this.coords.get(0).getX();
            x2 = this.coords.get(1).getX();
            y1 = this.coords.get(0).getY();
            y2 = this.coords.get(1).getY();
            
            w =  x1>=x2?x1-x2:x2-x1;
            
            h =  y1>=y2?y1-y2:y2-y1;
            
            return w * h;
        }
        else if((this.nombre).equals("Triangulo"))
        {
            double ax,ay,bx,by,cx,cy,aa,bb,cc,s;
            
            ax = this.coords.get(0).getX();
            ay = this.coords.get(0).getY();
            
            bx = this.coords.get(1).getX();
            by = this.coords.get(1).getY();
            
            cx = this.coords.get(2).getX();
            cy = this.coords.get(2).getY();
            
            cc = Math.sqrt((Math.pow((ax-bx),2) + Math.pow((ay-by),2)));
            aa = Math.sqrt((Math.pow((bx-cx),2) + Math.pow((by-cy),2)));
            bb = Math.sqrt((Math.pow((cx-ax),2) + Math.pow((cy-ay),2)));
            
            s =  (aa+bb+cc)   / 2;
            
            return Math.sqrt( (s * (s-aa) * (s-bb) * (s-cc)) );
        }
        return -1.0;
    }
    
    public double calcularPerimetro()
    {
        if((this.nombre).equals("Cuadrado"))
        {
            double w,h,x1,x2,y1,y2;
            x1 = this.coords.get(0).getX();
            x2 = this.coords.get(1).getX();
            y1 = this.coords.get(0).getY();
            y2 = this.coords.get(1).getY();
            w =  x1>=x2?x1-x2:x2-x1;
            h =  y1>=y2?y1-y2:y2-y1;
            
            return ( w + h ) * 2;
        }
        else if((this.nombre).equals("Triangulo"))
        {
            double ax,ay,bx,by,cx,cy,aa,bb,cc,s;
            
            ax = this.coords.get(0).getX();
            ay = this.coords.get(0).getY();
            
            bx = this.coords.get(1).getX();
            by = this.coords.get(1).getY();
            
            cx = this.coords.get(2).getX();
            cy = this.coords.get(2).getY();
            
            cc = Math.sqrt((Math.pow((ax-bx),2) + Math.pow((ay-by),2)));
            aa = Math.sqrt((Math.pow((bx-cx),2) + Math.pow((by-cy),2)));
            bb = Math.sqrt((Math.pow((cx-ax),2) + Math.pow((cy-ay),2)));
            
            s =  aa + bb + cc;
            
            return s;
        }
        
        return -1.0;
    }   
}
