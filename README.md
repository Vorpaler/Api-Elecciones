# Api-Elecciones

Como no encontraba documentacion sobre la ultima api para obtener los datos de las generales del 22 de octubre y me puse a investigarla y mediante prueba y error logre entender cual era el metodo pro el que que se manejan las peticiones a la URL base, de ahi se obtienen los datos del pais donde te van derivando a arrays de JSON con scopeId que vendrian a ser la URL que tenes que reemplazar en la base, referenciando asi cada uno a un nivel de granularidad mayor.
De esa forma podes ir navegando dentro de la api yendo por toda la informacion de cada provincia,seccion y ciudad.

Falta revisar que esten correctas las infos de todas las provincias por si no se granulan mas, ir agregando por distintos cargos (actualmente solo tiene el de candidatos a presidente) y abrir correctamente las secciones de Buenos Aires.

La idea de este codigo es la de facilitar el acceso a la informacion publica a cualquiera que quiera usar o saber los resultados de las elecciones, para asi controlarlas o trabajarlas o estudiarlas sin depender solo de los graficos que nos dan en la web.
