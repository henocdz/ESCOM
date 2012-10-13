package herencia;

public class Vivere extends Producto {

    private String caducidad;

    public Vivere()
    {
        super();
    }

     public Vivere(double precio,String marca,int ID,String caducidad)
   {
     super(precio,marca,ID);
     this.caducidad=caducidad;
   }


    public String getCaducidad()
            {
                return caducidad;
            }

    public void setCaducidad(String caducidad)
    {
        this.caducidad=caducidad;

    }


    @Override
    public void obtenerInformacion()
   {
       super.obtenerInformacion();
       System.out.println("Caducidad:"+getCaducidad());
   }


}
