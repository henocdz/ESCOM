/*
	Alumno: Henoc Diaz Hernandez
	Grupo: 2CM9
*/

function pressed (w) {
	var val = w.innerHTML;

	if(val=="=")
	{	
		check();
		return false;
	}

	addDigit(w.innerHTML);
}

function check()
{
	var obj = document.getElementById("iptext");


	if(obj.value==="")
	{	
		obj.style.backgroundColor = "rgba(56,56,56,0.5)";
		return false;
	}

	var parts = obj.value.split(".");

	if(parts.length !=  4)
	{
		obj.style.backgroundColor = "rgba(243,10,43,0.4)";
		return false;
	}

	var exp = /\D/g;
	for(i=0;i<parts.length;i++)
	{
		
		if(parts[i]==="" || parseInt(parts[i],10)>255 || parseInt(parts[i],10)<0 || exp.test(parts[i]))
		{
			obj.style.backgroundColor = "rgba(243,10,43,0.4)";
			return false;
		}	
	}

	obj.style.backgroundColor = "rgba(13,143,0,0.4)";
}

function addDigit(val)
{
	var obj = document.getElementById("iptext");
	var act = obj.value;

	act += val;

	obj.value = act;
	obj.focus();
	check();
}