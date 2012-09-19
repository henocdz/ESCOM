function doMagic () {

	var n = document.f.num.value;

	if(!(n%2 != 0) || n<=2)
	{
		alert("Debes introducir un numero y este debe ser impar");
		return false;
	}

	var cuadro = new Array(n);

	var i,j;
	i = j = 0;

	for(i;i<n;i++)
		cuadro[i] = new Array(n);

	//Inicializar cuadro
	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			cuadro[i][j] = null;

	//Guardar "coordenadas" de destino
	var lc = {
		y: 0,
		x: Math.round(n/2) - 1
	}

	//Respaldo para cuando "arriba a la derecha este ocupado por un numero"
	var bk = {
		y: 0,
		x: Math.round(n/2) - 1
	}

	//Iniciar llenado de cuadro
	cuadro[lc.y][lc.x] = 1;


	//Llenar cuadro
	for(j=2;j<=(n*n);j++)
	{	
		//Aplicar algoritmo "arriba a la derecha"
		lc.y -= 1;
		lc.x += 1;

		//Si se sale de los limites del arreglo se reinicia
		if(lc.y < 0)
			lc.y = n -1;

		if(lc.x>= n)
			lc.x = 0;

		//Si donde se busca poner es nulo se coloca
		if(cuadro[lc.y][lc.x] == null)
			cuadro[lc.y][lc.x] = j;
		else //Si no es nulo, esta ocupado por un numero y entonces se regresa al original  para ponerlo abajo
		{
			lc.y = bk.y +1;
			lc.x = bk.x;
			cuadro[lc.y][lc.x] = j;
		}

		bk.y = lc.y;
		bk.x = lc.x;
	}

	//Imprimir cuadro
	printcuadro(cuadro,n);
}


function printcuadro(c,n)
{
	var i,j;
	i = j = 0;
	var toPrint = "";
	var paper = document.getElementById("cuadro");

	for(i=0;i<n;i++)
	{
		toPrint += '<span class="rowSquare">';
		for(j=0;j<n;j++)
			toPrint += "  |  "+c[i][j]+"  |  ";

		toPrint += "</span> \n <br /><br />";
	}

	paper.innerHTML = toPrint;
	document.f.reset();
}