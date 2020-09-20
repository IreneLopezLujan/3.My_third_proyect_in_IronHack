
# Data-Pipelines

## “So many wines, so little time.”

![alt text](https://image.freepik.com/free-vector/cute-happy-smiling-wine-glass-cheese-cartoon-character-illustration-icon-design-isolated-white-background_92289-876.jpg)

### Vista

La finalidad de este proyecto es construir un pipeline que procese la data y devuelva un resultado.En este caso va a ser una recomendacion de vinos basado en el color del vino y el plato que se quiera comer con el vino. Ej white wine, salmon .... y te devolverá una seleccion de vinos que coincidan con ambas opciones.

Además se mostrarán las localizaciones de tiendas de vinos de tu ciudad. para ello utilizaremos la api de Google search que nos muestra los resultados de busqueda en tiempo real. El usuario de nuestro pipeline debe escribir la ciudad donde se encuentra y mostraremos un listado de tiendas de vino. Ej 'Madrid'---> La vinoteca de Sra, El Corte Inglés....

### Pasos

Para conseguir el dataframe que será filtrado hemos scrapeado un catalogo de vinos de decantalo.com y las comidas que machean con vinos de otro blog.Posteriormente se ha llevado a cabo limpieza y union de ellos.

El scraping en Google se ha llevado a cabo midiante una request, especificando contraseña a la api y parametros deseados.



### Ejemplo de Ejecución

Para correr el programa es necesario llamarlo desde la terminal de esta manera: python3 main.py y añadir los flags con los argumentos para la busqueda:-c (colores), -d (platos), -t(tiendas de vino de tu ciudad)

Ejemplo de ejecucion

> python3 main.py -c 'Sweet wine' -d 'Lamb' -t 'Madrid'

---- Los argumentos posibles con -c son los siguientes:
Ej: -c 'Sweet wine'  


'Fortified wine', 'Rosé wine', 'White wine', 'Red wine','Sweet wine', 'Orange wine'

---- Los argumentos posibles con -c son los siguientes:
Ej: -d 'Lamb'  

'Beef', 'Lamb', 'BBQ', 'Hamburger or Sausage', 'Chicken','Pasta','Lobster','Salmon'
'Pasta','Lighter Fish','Shellfish','Soft Cheeses','Goat Cheeses','Hard, Aged Cheeses','Feathered Game'

---- Los argumentos posibles con -d es cualquier ciudad en mente:
Ej: -t 'Madrid' 

'Madrid', 'Barcelona', 'París'...



### A Futuros....y en camino

Añadir el dato de precios y poder filtrar por rangos de precio los vinos. 
  

### Resources 

* [Python Functional Programming How To Documentation](https://docs.python.org/3.7/howto/functional.html)
* [Python List Comprehensions Documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [Python Errors and Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html)
* [StackOverflow String Operation Questions](https://stackoverflow.com/questions/tagged/string+python)
