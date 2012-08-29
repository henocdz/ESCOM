public class Main {
    public static void main(String args[])
    {
        Cuenta cuentas[] = new Cuenta[10];
        long numeros[] = {159753,369852,147852,258634,123456,789456,569823,569842,125634,569875};
        String nips[] = {"1234","4563","5698","5698","4569","8963","4782","4523","2620","5698"};
        double saldos[] = {0.0,123.50,50635.56,893.63,1520.34,2620.11,56983.45,456.26,5630.0,1563894.6};
        double intereses[] = {0.15,0.23,0,0.03,0.3,0.18,0.20,0.23,0.15,0.3};
        String clientes[] = {"Claudia Zizumbo","Daniel Perez","Sidia Martinez","Anna Ibarra","Adan Juarez","Eduardo Ibarra","Andrea Garcia","Uriel Hernandez","Ximena Bello","Henoc Diaz"};
        
        //Crear cuentas
        for(int i = 0;i<cuentas.length;i++)
            cuentas[i] = new Cuenta(numeros[i],nips[i],saldos[i],intereses[i],clientes[i]);    
        
        //Imprimir informacion
        for(int i = 0;i<cuentas.length;i++)
        {
            System.out.println("Cliente -> "+cuentas[i].getCliente());
            System.out.println("\t Numero -> "+cuentas[i].getNumero());
            System.out.println("\t Nip -> "+cuentas[i].getNip());
            System.out.println("\t Saldo -> "+cuentas[i].getSaldo());
            System.out.println("\t Interes Anual -> "+cuentas[i].getInteres());
            System.out.println("========================================================");            
        }
        
        //Cambiar Nip
        if((cuentas[1].getNip()).equals("56785"))
            System.out.println("La contraseña es igual a la actual");
        else
        {
            if(cuentas[1].setNip("56785"))
                System.out.print("La cuenta 2 ahora tiene el NIP: "+cuentas[1].getNip());
            else
                System.out.println("El NIP introducio no es válido");
        }
        
        //Transferencia entre cuentas
        if(cuentas[2].transfenciaCuentas(cuentas[4], 5000.45))
            System.out.print("Transferencia completada. \n La cuenta 3 tiene un saldo de: "+cuentas[2].getSaldo()+" \n La cuenta 5 tiene un saldo de: "+cuentas[4].getSaldo());
        else
            System.out.print("\n\n Saldo insuficiente para realizar transferencia");
        
        //Retirar saldo 
        if(cuentas[8].retirarSaldo(1560.8))
            System.out.print("\nRETIRO \n Se han retirado 1560.8 de la cuenta 9 \n Cuenta tiene un saldo de: "+cuentas[8].getSaldo());
        else
            System.out.println("No cuenta con saldo suficiente para retirar 1560.8 de la cuenta 9");
        
        //Consultar Saldo
        cuentas[7].consultarSaldo();
        
        
    }    
}
