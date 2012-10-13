package herencia;


public class Electrodomestico extends Producto {

   private int garantia=1;



   public Electrodomestico()
   {
     super();
   }

    public Electrodomestico(double precio,String marca,int ID,int garantia)
   {
     super(precio,marca,ID);
     this.garantia=garantia;
   }

   public int getGarantia()
   {
       return garantia;
   }

   public void setGarantia(int garantia)
   {
       this.garantia=garantia;

   }


    @Override
   public void obtenerInformacion()
   {
       super.obtenerInformacion();
       System.out.println("Garantia:"+getGarantia());
   }



}
