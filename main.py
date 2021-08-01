from tkinter import filedialog, Tk

def menu():
    print ("                                                                ")
    print ("---------------------------Bienvenido---------------------------")
    print ("|                                                              |")
    print ("|********Control Academico de la facultad de Ingenieria********|")
    print ("|                                                              |")
    print ("|  1. Carga de archivos.                                       |")
    print ("|  2. Mostrar reporte en consola.                              |")
    print ("|  3. Exportar reporte                                         |")
    print ("|  4. Salir.                                                   |")
    print ("----------------------------------------------------------------")

def cargaArchivo():
    Tk().withdraw()
    file = filedialog.askopenfile(
        title = "Selecciona un archivo, porfavor.",
        initialdir = "./",
        filetypes = (
            ("Únicamente .lfp", "*.lfp"),
            ("todos los archivos",  "*.*")
        )
    )
    if file is None:
        print("No has seleccioado ningun archivo.")
        return None
    else:
        datos = file.read()
        file.close()
        print("Tu archivo ha sido cargado exitosamente.")
        return datos

while True:
    menu()
    select = int(input("Selecciona alguna opción:"))

    if select == 1:
        print ("Cargaaa")
        txt = cargaArchivo()
    elif select == 2:
        print("Mostrar")
    elif select == 3:
        print("Repoconso")
    elif select == 4:
        print ("------          Gracias por usar mi programa :3           ------")
        print ("----------------------------------------------------------------")
        break
    else:
        print("No existe esa opción")