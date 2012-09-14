
package Banco;
import java.util.*;
public class Cliente {
    private String nombre,apellidos,direccion,localidad;
    private Date fNacimiento;
    
    
    public Cliente(String nombre,String apellidos,String direccion, String localidad, Date fNacimiento)
    {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.direccion = direccion;
        this.localidad = localidad;
        this.fNacimiento = fNacimiento;
    }
    
    public String nombreCompleto()
    {
        return this.nombre + " " + this.apellidos;
    }
    
    public String direccionCompleta()
    {
        return this.direccion + " " + this.localidad;
    }
    
    public Date getFNacimiento()
    {
        return this.fNacimiento;
    }
}
