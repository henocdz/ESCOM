function doMagic (n) {
	var c = document.getElementById('status');
	var x;
	if(n%2 == 0)
	{
		x = n/2;
		c.innerHTML = c.innerHTML + "<br /> Par y "+n+" != 1 || Operacion: (" + n + "/2) =  " +x;
		if(x == 1){
			c.innerHTML = c.innerHTML + "<br /> El numero es maravilloso"
			return false;
		}
		
		doMagic(x)
	}
	else
	{
		x = (n*3)+1;
		c.innerHTML = c.innerHTML + "<br /> Impar  y "+n+" != 1 // Operacion: (" + n + "*3)+1 =  " +x;

		if(x==1){
			c.innerHTML = c.innerHTML + "<br /> El numero es maravilloso"
			return false;
		}

		
		doMagic(x);
	}
}

function go(n)
{
	document.getElementById('status').innerHTML = "";
	doMagic(n);
}