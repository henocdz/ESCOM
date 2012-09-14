package Figuras;

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Roofdier
 */
public class Punto {
    double coordX,coordY;
    
    public Punto()
    {
        this.coordX = 1.0;
        this.coordY = 3.0;
    }
    
    public Punto(double x,double y)
    {
        this.coordX = x;
        this.coordY = y;
    }
    
    public double getX()
    {
        return this.coordX;
    }
    
    public double getY()
    {
        return this.coordY;
    }
    
    public void setX(double x)
    {
        this.coordX = x;
    }
    
    public void setY(double y){
        this.coordY = y;
    }
}
