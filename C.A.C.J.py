import os
import json
import requests
#Conexion a Api y Creacion de JSON
def get_data_recursively(scope_id):
    url = f"https://resultados.gob.ar/backend-difu/scope/data/getScopeData/{scope_id}/1/1"
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except json.JSONDecodeError:
            print(f"Error: La respuesta para scopeId {scope_id} no es un JSON válido.")
            return  

data = get_data_recursively("00000000000000000000000b")
mapa = data["mapa"]

prov = {}  # Un diccionario para almacenar las provincias y sus scopeId

for provincia in mapa:
    for scope in provincia.get("scopes", []):
        prov[scope["name"]] = scope["scopeId"]

# Ahora puedes acceder a los 'scopeId' de las provincias en el diccionario 'prov'
# Por ejemplo, para obtener el 'scopeId' de una provincia específica:

for provincia, scope_id in prov.items():
    #print(f"Para la Provincia: {provincia}, scopeId: {scope_id}")

    # Obtenemos la sección para la provincia actual
    section = get_data_recursively(scope_id)["mapa"][0]["scopes"]

    # Creamos un directorio para la provincia si no existe
    province_folder = os.path.join("resultados_elecciones", provincia)
    os.makedirs(province_folder, exist_ok=True)

    # Iteramos sobre las secciones y guardamos sus datos en archivos JSON
    for sec in section:
        sec_name = sec["name"]
        sec_scope_id = sec["scopeId"]
        
        #print(f"Para la sección/ciudad {sec_name}, su scopeId es {sec_scope_id}")

        # Guardamos el JSON de 'sec' en un archivo dentro de la carpeta de la provincia
        if(provincia != "Buenos Aires"):
            with open(os.path.join(province_folder, f'{sec_name}.json'), 'w') as file:
                json.dump(sec, file, indent=4)
        else:
            i = 0
            for ciudades in sec["scopeId"]:
                ciudad = get_data_recursively(ciudades)
                i = i+1
                print("################################################ " + str(i) + " " + str(sec["scopeId"]))
                #print("Esta es una ciudad:" + ciudad)
        
