package Banco;

import java.util.*;
import java.text.*;
public class Main {
    public static void main(String args[])
    {

        
        Cliente c1,c2,c3;
        ArrayList<Cuenta> cuentas = new ArrayList();
        ArrayList<Cliente> clientes = new ArrayList();
        int it,itc;
        
        SimpleDateFormat d = new SimpleDateFormat("dd/MM/YYYY");
        
        
        it = itc = 0;
           
        clientes.add(new Cliente("Mauricio","Jiménez García","Saltillo 135","Lomas de Chapultepec",new GregorianCalendar(1989,Calendar.JANUARY,27).getTime()));
        clientes.add(new Cliente("Andrea","Pérez Suárez","Av. Lindavista s/n","Tores Lindavista",new GregorianCalendar(1992,Calendar.AUGUST,12).getTime()));
        clientes.add(new Cliente("José Manual","Marquez","Calle 5 No. 17","Coyoacan",new GregorianCalendar(1972,Calendar.NOVEMBER,22).getTime()));
        
        cuentas.add(new Cuenta(clientes.get(0),21545612,145622.50,0.0));
        cuentas.add(new Cuenta(clientes.get(0),6512629,5000.0,0.05));

        
        cuentas.add(new Cuenta(clientes.get(1),63555655,61252.80,0.03));
        cuentas.add(new Cuenta(clientes.get(1),4121852,58600.0,0.05));
        
        cuentas.add(new Cuenta(clientes.get(2),1265655,12352.80,0.0));
        cuentas.add(new Cuenta(clientes.get(2),1541512,56022.80,0.03));
        cuentas.add(new Cuenta(clientes.get(2),123151561,125236.80,0.02));

        //Movimientos cuenta 1
        cuentas.get(0).realizarMovimiento(new GregorianCalendar(2012,Calendar.AUGUST,10).getTime(), "Retiro", 1500);
        cuentas.get(0).realizarMovimiento(new GregorianCalendar(2012,Calendar.SEPTEMBER,12).getTime(), "Ingreso", 400.50);
        cuentas.get(0).realizarMovimiento(new GregorianCalendar(2012,Calendar.SEPTEMBER,13).getTime(), "Consulta Saldo",0);
        
        cuentas.get(1).realizarMovimiento(new GregorianCalendar(2012,Calendar.AUGUST,8).getTime(), "Retiro", 200);
        cuentas.get(1).realizarMovimiento(new GregorianCalendar(2012,Calendar.SEPTEMBER,12).getTime(), "Pago Tarjeta", 400.5);        
        cuentas.get(1).realizarMovimiento(new GregorianCalendar(2012,Calendar.AUGUST,10).getTime(), "Retiro", 1500);
        
        cuentas.get(2).realizarMovimiento(new GregorianCalendar(2012,Calendar.JANUARY,18).getTime(), "Retiro", 200);
        cuentas.get(2).realizarMovimiento(new GregorianCalendar(2012,Calendar.JULY,16).getTime(), "Retiro", 980);      
        cuentas.get(2).realizarMovimiento(new GregorianCalendar(2012,Calendar.AUGUST,12).getTime(), "Pago Servicio", 350.6);
        
        
        cuentas.get(4).realizarMovimiento(new GregorianCalendar(2012,Calendar.JULY,3).getTime(), "Consulta Saldo",0);
        
        
        cuentas.get(5).realizarMovimiento(new GregorianCalendar(2012,Calendar.MAY,14).getTime(), "Retiro", 500);
        cuentas.get(5).realizarMovimiento(new GregorianCalendar(2012,Calendar.SEPTEMBER,11).getTime(), "Ingreso", 1250.5);
        
        cuentas.get(6).realizarMovimiento(new GregorianCalendar(2012,Calendar.APRIL,3).getTime(), "Ingreso", 1500);
        cuentas.get(6).realizarMovimiento(new GregorianCalendar(2012,Calendar.JUNE,5).getTime(), "Retiro", 4025.5);
        
        
        for(Cliente c: clientes)
        {
            it++;
            itc = 0;
            
            System.out.println("\n\nCliente "+it+"\n\t Nombre: "+c.nombreCompleto()+"\n\t Dirección: "+c.direccionCompleta()+"\n\t Fecha de Nacimiento: "+ d.format(c.getFNacimiento()) );
            
            for(Cuenta cc: cuentas)
            {
                if(cc.getTitular().equals(c.nombreCompleto()))
                {   
                    itc++;
                    System.out.println("\nCuenta "+ itc);
                    cc.imprimirInfoCuenta();
                }
            }
        }
        
        
        
        
        
        
    }
}
