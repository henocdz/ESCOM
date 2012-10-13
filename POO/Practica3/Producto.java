package herencia;

public class Producto {

    protected double precio;
    protected String marca;
    protected int ID;


    public Producto()
    {
    }

    public Producto(double precio,String marca,int ID)
    {
        this.precio=precio;
        this.marca=marca;
        this.ID=ID;
    }

    public double getPrecio()
    {
        return precio;

    }

    public void setPrecio(double precio)
    {
        this.precio=precio;
    }


    public String getMarca()
    {
        return marca;

    }

    public void setMarca(String marca)
    {
        this.marca=marca;

    }

    public int getID()
    {
        return ID;

    }

    public void setID(int ID)
    {
        this.ID=ID;

    }

    public void obtenerInformacion()
   {
       System.out.println("La informacion del producto: ");
       System.out.println("Marca: "+ getMarca());
       System.out.println("Precio: "+ getPrecio());
       System.out.println("ID: "+ getID());
   }


}
