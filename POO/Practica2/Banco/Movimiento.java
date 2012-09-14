package Banco;

import java.util.*;
public class Movimiento {
    private Date fecha;
    private String tipo;
    private double importe;
    private double saldo;
    
    public Movimiento(Date fecha,String tipo,double importe, double saldo)
    {
        this.fecha = fecha;
        this.tipo = tipo;
        this.importe = importe;
        this.saldo = saldo;
    }
    
    public Date getFecha()
    {
        return this.fecha;
    }
    
    public String getTipo()
    {
        return this.tipo;
    }
    
    public double getImporte()
    {
        return this.importe;
    }
    
    public double getSaldo()
    {
        return this.saldo;
    }
}
