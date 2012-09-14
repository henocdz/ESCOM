package Banco;

import java.util.*;

public class Cuenta {
    private long numero;
    private String titular;
    private double saldo;
    private double interesAnual;
    private ArrayList <Movimiento> movimientos = new ArrayList();
    
    public Cuenta(Cliente c,long id,double saldo, double interes)
    {
        this.titular = c.nombreCompleto();
        this.numero = id;
        this.saldo = saldo;
        this.interesAnual = interes;
    }
    
    public double getSaldo()
    {
        return this.saldo;
    }
    
    public String getTitular()
    {
        return this.titular;
    }
    
    public boolean realizarMovimiento(Date fecha,String tipo,double importe)
    {
        if(tipo.toLowerCase().equals("retiro"))
        {
            if(!(this.saldo - importe >= 0))
                return false;
            else
                this.saldo -= importe;
        }else if(tipo.toLowerCase().equals("ingreso"))
        {
            this.saldo += importe;
        }
        
        Movimiento move = new Movimiento(fecha,tipo,importe,this.saldo);
        this.movimientos.add(move);
        
        return true;
    }
    
    public void imprimirMovimientos()
    {
        System.out.print("\nMovimientos: ");
        if(this.movimientos.isEmpty())
        { 
            System.out.print("No Hay");
            return;
        }
        
        int it = 0;
        for(Movimiento m:this.movimientos)
        {
            it += 1;
            
            int d,mm,a;
            String ff;
            
            d = m.getFecha().getDay();
            mm = m.getFecha().getMonth() + 1;
            a = m.getFecha().getYear();
            ff = d+"/"+mm+"/"+a;
            
            System.out.print("\n\t Movimiento: "+it+": \n\t\t Tipo: " + m.getTipo() + "\n\t\t Fecha: "+ ff +" \n\t\t Importe: "+m.getImporte()+"\n\t\t Saldo: " +m.getSaldo());
        }
    }
    
    public void imprimirInfoCuenta()
    {
        System.out.println("\t Número: "+this.numero+" \n\t Saldo: "+this.saldo+"\n\t Interés:"+this.interesAnual);
        
        this.imprimirMovimientos();
    }
    
    public void ingreso(double cantidad)
    {
    }
    
    public void reintegro(double cantidad)
    {
        
    }
}
