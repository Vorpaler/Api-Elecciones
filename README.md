# Api-Elecciones

Como no encontraba documentacion sobre la ultima api para obtener los datos de las generales del 22 de octubre y me puse a investigarla y mediante prueba y error logre entender que se manejan desde una URL base, de ahi se obtienen los datos del pais donde te van derivando a arrays de JSON con scopeId que vendrian a ser la URL que tenes que reemplazar, referenciando asi cada uno a un nivel de granularidad mayor.
De esa forma podes ir navegando dentro de la api yendo por toda la informacion de cada provincia,seccion y ciudad.

Falta revisar que esten correctas las infos de todas las provincias, esto es, si no se granulan mas, ir agregando por distintos cargos ademas de presidente y abrir correctamente las secciones de Buenos Aires.

Cualquiera que quiera obtener los datos para su uso podra usar este codigo libremente para revisar los datos y trabajarlos como quieran.
