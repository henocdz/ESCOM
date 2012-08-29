class Circulo
{
	
	//Atributos
	private double radio;
	private double area;
	private double perimetro;

	//Contructor por parametros
	public Circulo(double radio)
	{
		this.radio = radio;
		this.perimetro = this.calcularPerimetro();
		this.area = this.calcularArea();
	}
	
	//Constructor po omision
	public Circulo()
	{
		this.radio = 3.0;	
		this.perimetro = this.calcularPerimetro();
		this.area = this.calcularArea();	
	}
	
	//Constructor por copia
	public Circulo(Circulo o)
	{
		this.radio = o.radio;
		this.perimetro = o.perimetro;
		this.area = o.area;
	}
	
	
	//Metodos
	public double getRadio()
	{
		return this.radio;
	}

	public void setRadio(double radio)
	{
		this.radio = radio;
	}

	public double getArea()
	{
		return this.calcularArea();
	}	
		
	public double getPerimetro()
	{
		return this.calcularPerimetro();
	}

	public double calcularArea()
	{
		double a = Math.PI * (this.radio * this.radio);
		this.area = a;
		return a;
	}

	public double calcularPerimetro()
	{
		double p = Math.PI * (this.radio * 2);
		this.perimetro = p;
		return p;
	}

}