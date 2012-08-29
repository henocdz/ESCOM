class Triangulo {
	
	//Atributos
	private double l1,l2,l3,perimetro,area;
	
	
	//Constructor por omision
	public Triangulo()
	{
            this.l1 = 1.0;
            this.l2 = 1.0;
            this.l3 = 1.0;
            
            this.perimetro = this.calcularPerimetro();
            this.area = this.calcularArea();
	}
	
	//Constructor por parametro, triangulo equilatero
	public Triangulo(double l)
	{
            this.l1 = this.l2 = this.l3 = l;
	}
	
	//Constructor por parametros, triangulo isoceles
	public Triangulo(double l_igual,double l_diferente)
	{
            this.l1 = this.l2 = l_igual;
            this.l3 = l_diferente;
	}
	
	//Constructor por parametros, triangulo escaleno
	public Triangulo(double altura,double base, double l3)
	{
            this.l1 = altura;
            this.l2 = base;
            this.l3 = l3;
	}
	
	//Constructor por copia	
	public Triangulo(Triangulo other)
	{
            this.l1 = other.l1;
            this.l2 = other.l2;
            this.l3 = other.l3;
            this.perimetro = other.perimetro;
            this.area = other.perimetro;
	}
	
	
	//Metodos
	public void setLado(double l)
	{
            this.l3 = this.l2 = this.l1 = l;
	}
	
	public double getLado()
	{
            return this.l1;
	}
	
	public double getPerimetro()
	{
            return this.calcularPerimetro();
	}

	public double getArea()
	{
            return this.calcularArea();
	}
	
	public double calcularArea()
	{
            //Si es escaleno...
            if((this.l1 != this.l2) && (this.l2 != this.l3) && (this.l3 != this.l1))
                return (this.l1 * this.l2)/2;

            double b = this.l3/2;
            //Obtener altura (Pitagoras)

            double h = Math.sqrt(Math.pow(this.l1,2) - Math.pow(b,2));
            return b * h / 2;
	}
	
	public double calcularPerimetro()
	{
            return this.l1 + this.l2 + this.l3;
	}
	
}
