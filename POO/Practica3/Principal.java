package herencia;

import java.util.*;
public class Principal {

     public static void main (String args[])
    {
        ArrayList<Vivere> vs = new ArrayList();
        ArrayList<Electrodomestico> es = new ArrayList();

     
        es.add(new Electrodomestico(5250,"MABE",5879,3));
        es.add(new Electrodomestico(4550,"E&G",879,5));

        vs.add(new Vivere(10.5,"ALPURA",55,"02/05/2012"));
        vs.add(new Vivere(8.5,"LALA",250,"02/10/2012"));
        
        while(true){
            int op = GUI.menu();
            int c;
            if(op==1)
            {//Mostrar electrodomestico
                op = GUI.mostrarMenuElectrodom(vs.size()); //Menu
                c = GUI.mostrarElectrodom(es.get(op-1)); //Info
                
                if(c == 0)//Cocontinaur compra
                {
                    c = GUI.mostrarUltima();
                    if(c == 1)
                    {/* Aquí iría lo de TICKET*/}
                    else
                        continue;
                }else{//Regresar al menu
                    continue;
                }
                
            }else if(op == 2){//Mostrar vivere
                op = GUI.mostrarMenuVivere(es.size()); //Menu
                c = GUI.mostrarVivere(vs.get(op-1)); //Info

                if(c == 0)//Continuar compra
                {
                    c = GUI.mostrarUltima();
                    if(c == 1)
                    {/* Aquí iría lo de TICKET*/}
                    else
                        continue;
                }else{//Regresar al menu
                    continue;
                }
            }

           }
    }
}
