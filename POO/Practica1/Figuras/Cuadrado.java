class Cuadrado
{
	//Atributos
	private double lado;
	private double area;
	private double perimetro;
	
	//Constructor por parametro
	public Cuadrado(double lado)
	{
		this.lado = lado;
		this.area = this.calcularArea();
		this.perimetro = this.calcularPerimetro();
	}
	
	//Constructor por omision
	public Cuadrado()
	{
		this.lado = 2;
		this.area = this.calcularArea();
		this.perimetro = this.calcularPerimetro();
	}
	
	//Constructor por copia
	public Cuadrado(Cuadrado c)
	{
		this.lado = c.lado;
		this.area = c.getPerimetro();
		this.perimetro = c.getArea();
	}
	
	
	//Getters & Setters
	public double getLado()
	{
		return this.lado;
	}

	public void setLado(double lado)
	{
		this.lado = lado;
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
		double a = this.lado * this.lado;
		this.area = a;
		return a;
	}

	public double calcularPerimetro()
	{
		double p = this.lado * 4;
		this.perimetro = p;
		return p;
	}
	
}