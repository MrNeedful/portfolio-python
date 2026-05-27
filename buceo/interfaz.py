import tkinter as tk
from diving import cargar_inmersiones, nuevas_inmersiones, guardar_inmersiones, prof_max, prof_min, mas_duracion, filtrar_por_ubicacion, ver_inmersiones, inmersiones

ventana = tk.Tk()
ventana.title("🤿 Diving Log")
area = tk.Text(ventana, width=60, height=20)
area.pack()
def mostrar_ver_inmersiones():
    area.delete("1.0", tk.END)
    for inmersion in inmersiones:
        area.insert(tk.END, f'🤿 {inmersion['sitio']} - {inmersion['ubicacion']}\n')
        area.insert(tk.END, f' {inmersion['profundidad_maxima']} mts - {inmersion['duracion']} mins - {inmersion['visibilidad_porcentaje']}%\n')

def mostrar_prof_max():
    area.delete("1.0", tk.END)
    area.insert(tk.END, f'Profundidad máxima: {prof_max()} mts')
        
def mostrar_prof_min():
    area.delete("1.0", tk.END)
    area.insert(tk.END, f'Profundidad minima: {prof_min()} mts')
        
def mostrar_mas_duracion():
    area.delete("1.0", tk.END)
    area.insert(tk.END, f'Inmersión más larga: {mas_duracion()} mins')
    
btn_ver = tk.Button(ventana, text="Ver Inmersiones", command=mostrar_ver_inmersiones)
btn_ver.pack()
btn_max = tk.Button(ventana, text="Profundiad Maxima", command=mostrar_prof_max)
btn_max.pack()
btn_min = tk.Button(ventana, text="Profundidad Minima", command=mostrar_prof_min)
btn_min.pack()
btn_duracion = tk.Button(ventana, text="Mas Duracion", command=mostrar_mas_duracion)
btn_duracion.pack()



ventana.mainloop()