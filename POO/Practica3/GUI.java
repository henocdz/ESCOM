/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package herencia;
import javax.swing.JOptionPane;


/*
 * La clase es abstracta
 * por eso no se necesitan instancias
 * es como JOptionPane
 */

public abstract class GUI {
    JOptionPane p;
   private static String o;
   private static int op;
   public GUI(){
       o = "-1";
       try{
           op = Integer.parseInt(o);
       }catch(Exception e){
           
       }
   }
   
   public static int menu(){
       o = JOptionPane.showInputDialog(null,"Opciones: \n 1.- Electrodomesticos \n 2.- Viveres \n 3.- Salir \n Seleccione una opción: ","Productos",JOptionPane.INFORMATION_MESSAGE);
       boolean flag = false;

       if(o == null)
           System.exit(1);
       
       try{
           op = Integer.parseInt(o);
           
           if (op == 3)
               System.exit(1);
           else if(op>3 || op<1)
               op = menu();
           flag = true;
       }catch(Exception e){
           JOptionPane.showMessageDialog(null, "Dato invalido, intente de nuevo", "Error", JOptionPane.ERROR_MESSAGE);
           op = menu();
       }
       
       return op;
   }
    
public static int mostrarMenuElectrodom(int l){
      o = JOptionPane.showInputDialog(null,"Opciones: \n 1.- Pantalla TV \n 2.- Computadora \n Seleccione una opción: ","Electrodomesticos",JOptionPane.INFORMATION_MESSAGE);
       boolean flag = false;
       
       if(o == null)
           o = String.valueOf(mostrarMenuElectrodom(l));
       
       try{
           op = Integer.parseInt(o);
           flag = true;
           
            if(op>l || op<1)
               op = mostrarMenuElectrodom(l);
       }catch(Exception e){
           JOptionPane.showMessageDialog(null, "Dato invalido, intente de nuevo", "Error", JOptionPane.ERROR_MESSAGE);
           op = mostrarMenuElectrodom(l);
       }
       
       return op;
   }
   
   public static int mostrarMenuVivere(int l){
       
       o = JOptionPane.showInputDialog(null,"Opciones: \n 1.- Leche \n 2.- Galletas \n Seleccione una opción: ","Electrodomesticos",JOptionPane.INFORMATION_MESSAGE);
       boolean flag = false;
       
       if(o == null)
           o = String.valueOf(mostrarMenuVivere(l));
       
       try{
           op = Integer.parseInt(o);
            
           if(op>l || op<1)
               op = mostrarMenuVivere(l);
           flag = true;
       }catch(Exception e){
           JOptionPane.showMessageDialog(null, "Dato invalido, intente de nuevo", "Error", JOptionPane.ERROR_MESSAGE);
           op = mostrarMenuVivere(l);
       }
       
       return op;
   }
   
   public static int mostrarVivere(Vivere v){
       
       
       return JOptionPane.showConfirmDialog(null, "ID: "+v.getID()+" \nPrecio:"+v.getPrecio()+"\nMarca:"+v.getMarca()+"\nCaducidad:"+v.getCaducidad(), "Comprar", JOptionPane.INFORMATION_MESSAGE);

   }
   
   public static int mostrarElectrodom(Electrodomestico e){
       
       return JOptionPane.showConfirmDialog(null,"ID: "+e.getID()+" \nPrecio:"+e.getPrecio()+"\nMarca:"+e.getMarca()+"\nGarantia:"+e.getGarantia(), "Comprar", JOptionPane.INFORMATION_MESSAGE);
   }
   
   public static int mostrarUltima(){
       o = JOptionPane.showInputDialog(null,"1.- Regresar al menu \n2.- Generar ticket \n Seleccione una opción: ","Electrodomesticos",JOptionPane.INFORMATION_MESSAGE);
       boolean flag = false;
       
       if(o == null)
           o = String.valueOf(mostrarUltima());
       
       try{
           op = Integer.parseInt(o);
           flag = true;
           
            if(op>2 || op<1)
               op = mostrarUltima();
       }catch(Exception e){
           JOptionPane.showMessageDialog(null, "Dato invalido, intente de nuevo", "Error", JOptionPane.ERROR_MESSAGE);
           op =mostrarUltima();
       }
       
       return op;
   }
}
