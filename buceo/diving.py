import json

def cargar_inmersiones():
    with open('archivo.json', 'r') as archivo:
       return json.load(archivo) 

def guardar_inmersiones():
    with open('archivo.json', 'w') as archivo:
        json.dump(inmersiones, archivo)
        
def nuevas_inmersiones():

    sitio = input('Sitio de la inmersion: ')
    ubicacion = input('Ubicacion: ').lower()
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
        

def prof_max():
    mas_profunda = 0 
    
    for inmersion in inmersiones:
        if inmersion['profundidad_maxima'] > mas_profunda:
            mas_profunda = inmersion['profundidad_maxima']
    return mas_profunda



def mas_duracion():
    duracion_max = 0 
    
    for inmersion in inmersiones:
        if inmersion['duracion'] > duracion_max:
            duracion_max = inmersion['duracion']
    return duracion_max

def prof_min():
    menos_profunda = float('inf')
    
    for inmersion in inmersiones:
        if inmersion['profundidad_maxima'] < menos_profunda:
            menos_profunda = inmersion['profundidad_maxima']
            
    return menos_profunda


def filtrar_por_ubicacion():
    ubicacion_usuario = input('Introduce una ubicacion: ').lower()
    resultados = []
    for inmersion in inmersiones:
        if inmersion['ubicacion'] == ubicacion_usuario:
            resultados.append(inmersion)
    return resultados




def mostrar_menu():
    while True:
        print('1. nuevas_inmersiones') 
        print('2. prof_max')  
        print('3. prof_min')  
        print('4. mas duracion') 
        print('5. Filtrar por ubicacion') 
        print('6. Salir') 
        opcion = (input("Elije una de las Opciones: "))
            
        match opcion:
                case '1':
                    print(nuevas_inmersiones())
                case '2':
                    print(prof_max())
                    input("Presioná Enter para continuar...")
                case '3':
                    print(prof_min())
                    input("Presioná Enter para continuar...")
                case '4':
                    print(mas_duracion())
                    input("Presioná Enter para continuar...")
                case '5':
                    print(filtrar_por_ubicacion())
                    input("Presioná Enter para continuar...")
                case '6':
                    break
                case _:
                    print('Opcion no valida') 
                    

                       
inmersiones = cargar_inmersiones()
mostrar_menu()
    
        
        
        






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





    
        
    
    
    
