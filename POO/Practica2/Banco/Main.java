package Banco;

import java.util.*;
public class Main {
    public static void main(String args[])
    {

        
        Cliente c1,c2,c3;
        ArrayList<Cuenta> cuentas = new ArrayList();
        ArrayList<Cliente> clientes = new ArrayList();
        int it,itc;
        
        it = itc = 0;
        
        clientes.add(new Cliente("Mauricio","Jiménez García","Saltillo 135","Lomas de Chapultepec",new Date(1989,0,27)));
        clientes.add(new Cliente("Andrea","Pérez Suárez","Av. Lindavista s/n","Tores Lindavista",new Date(1992,7,12)));
        clientes.add(new Cliente("José Manual","Marquez","Calle 5 No. 17","Coyoacan",new Date(1972,10,22)));
        
        cuentas.add(new Cuenta(clientes.get(0),21545612,145622.50,0.0));
        
        cuentas.get(0).realizarMovimiento(new Date(2012,7,10), "Retiro", 1500);
        cuentas.get(0).realizarMovimiento(new Date(2012,8,12), "InGrEso", 400.50);
        
        for(Cliente c: clientes)
        {
            it++;
            
            int d,m,a;
            String ff;
            
            d = c.getFNacimiento().getDay();
            m = c.getFNacimiento().getMonth() +1;
            a = c.getFNacimiento().getYear();
            ff = d+"/"+m+"/"+a;
            
            System.out.println("\n\nCliente "+it+"\n\t Nombre: "+c.nombreCompleto()+"\n\t Dirección: "+c.direccionCompleta()+"\n\t Fecha de Nacimiento: "+ff);
            
            for(Cuenta cc: cuentas)
            {
                if(cc.getTitular().equals(c.nombreCompleto()))
                {   
                    itc++;
                    System.out.println("Cuenta "+ itc);
                    cc.imprimirInfoCuenta();
                }
            }
        }
        
        
        
        
        
        
    }
}
