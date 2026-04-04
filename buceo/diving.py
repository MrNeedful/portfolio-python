import json

def cargar_inmersiones():
    with open('archivo.json', 'r') as archivo:
       return json.load(archivo) 

def guardar_inmersiones():
    with open('archivo.json', 'w') as archivo:
        json.dump(inmersiones, archivo)
        
def nuevas_inmersiones():

    sitio = input('Sitio de la inmersion: ')
    ubicacion = input('Ubicacion: ')
    profundidad_maxima = float(input('Cual fue la maxima profundidad: '))
    duracion = int(input('Tiempo total de la inmersion: '))
    temp_superficie = float(input('Que temperatura de superficie habia?: '))
    temp_fondo = float(input('Que temperatura de fondo habia?: '))
    visibilidad_porcentaje = int(input('Visibilidad %: '))
    respuesta = input("¿Hiciste parada de seguridad? (s/n): ")
    parada_de_seguridad = respuesta == "s"
    
    inmersiones.append({'sitio': sitio,
                            'ubicacion': ubicacion,
                            'profundidad_maxima': profundidad_maxima,
                            'duracion': duracion,
                            'temp_superficie': temp_superficie,
                            'temp_fondo': temp_fondo,
                            'visibilidad_porcentaje': visibilidad_porcentaje,
                            'parada_de_seguridad': parada_de_seguridad}
                       )
        

inmersiones = cargar_inmersiones()


nuevas_inmersiones()
guardar_inmersiones()
print(inmersiones)



# inmersiones = [{'sitio': 'Don Pedro',
#                 'ubicacion': 'Ibiza', 
#                 'profundidad_maxima': 42, 
#                 'duracion': 37, 
#                 'temp_superficie': 22, 
#                 'temp_fondo': 18, 
#                 'visibilidad_porcentaje': 89, 
#                 'parada_de_seguridad': True}
#                ]

# inmersiones.append({'sitio': 'Plataforma Mariana',
#                 'ubicacion': 'Formentera', 
#                 'profundidad_maxima': 38, 
#                 'duracion': 40, 
#                 'temp_superficie': 23, 
#                 'temp_fondo': 20, 
#                 'visibilidad_porcentaje': 90, 
#                 'parada_de_seguridad': True})





    
        
    
    
    
