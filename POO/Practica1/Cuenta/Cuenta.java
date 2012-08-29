public class Cuenta {
    
    //Atributos
    private long numero;
    private String nip;
    private double saldo;
    private double interesAnual;
    private String cliente;
    
    /*
     ********* Constructores
    */
    
    //Constructor por omisión
    public Cuenta()
    {
        this.numero = 1234567890;
        this.nip = "0569";
        this.interesAnual = 0.15;
        this.cliente = "Anonymous";
    }
    
    //Constructor por copia
    public Cuenta(Cuenta fake)
    {
        this.numero = fake.numero;
        this.nip = fake.nip;
        this.interesAnual = fake.interesAnual;
        this.cliente = fake.cliente;
    }
    
    //Constructor por parametros
    public Cuenta(long numero,String nip,double saldo, double interesAnual,String cliente)
    {
        this.numero = numero;
        this.nip = nip;
        this.saldo = saldo;
        this.interesAnual = interesAnual;
        this.cliente = cliente;
    }
    
    //Metodos
    public long getNumero()
    {
        return this.numero;
    }
    
    public void setNumero(long numero)
    {
        this.numero = numero ;
    }
    
    public String getNip()
    {
        return this.nip;
    }
    
    public boolean setNip(String nip)
    {
        boolean flag = true;
        int i = 0;
        while(flag && i < nip.length())
        {
            if(!Character.isDigit(nip.charAt(i)))
                flag = false;
            
            i++;
        }

        if(nip.length()>4 || flag == false)
            return false;
        
        this.nip = nip;
        return true;
    }
    
    public double getInteres()
    {
        return this.interesAnual;
    }
    
    public void setInteres(double interes)
    {
        this.interesAnual = interes;
    }
    
    public double getSaldo()
    {
        return this.saldo;
    }
    
    public void setSaldo(double saldo)
    {
        this.saldo = saldo;
    }
    
    
    public String getCliente()
    {
        return this.cliente;    
    }
    
    public void setCliente(String cliente)
    {
        this.cliente = cliente;
    }
    
    public boolean cambiarNip(String nip)
    {      
        if(this.setNip(nip))
            return true;
        else 
            return false;
    }
    
    //Segun el diagrama dado en clase solo debe imprimir el saldo, por eso regresa void
    protected void consultarSaldo()
    {
        System.out.print("\n\n Tiene un total de: " + this.saldo);
    }
    
    public boolean retirarSaldo(double monto)
    {
        if(monto >= 0 && this.saldo >= monto)
        {
            this.saldo -= monto;
            return true;
        }
        else
            return false;
    }
    
    public boolean transfenciaCuentas(Cuenta des,double monto)
    {
        if(this.retirarSaldo(monto))
        {
            des.setSaldo(des.getSaldo() + monto);
            return true;
        }
        else 
            return false;
    }
    
}
