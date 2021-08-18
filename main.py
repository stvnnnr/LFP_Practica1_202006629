from tkinter import filedialog, Tk #Importo metodos de lectura de archivos
from Estudiante import Estudiante #Importo la clase estudiante que me sera util
#Declaro mis variables globales a usar
global parameters
students = []
ascendente = []
descendente = []
listaGanadores = []
listaPerdedores = []
global promedio
global nameCurse
global notaMayor
global notaMenor
global numberStudents
global ganadores
global perdedores

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
    #Utilizo en metodo para generar una ventana para poder cargar mi archivo lfp y pasarlo a una variable
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


    print("aca empezamos")

def separarpalabras():
    #primero defino mis variables globales a usar
    global students
    global ascendente
    global descendente
    global listaGanadores
    global listaPerdedores
    global parameters
    global promedio
    global nameCurse
    global notaMayor
    global notaMenor
    global numberStudents
    global ganadores
    global perdedores


    textPlano = cargaArchivo()#Paso mi archivo cargado a una variable y comienzo a separarlas
    textSeparadoUno = textPlano.split(" = {\n")
    nameCurse = textSeparadoUno[0]#obtengo el nombre del curso
    textAsepararDos = textSeparadoUno[1]
    textSeparadoDos = textAsepararDos.split("\n} ")
    studentSinSeparar = textSeparadoDos[0]
    parameterSinSeparar = textSeparadoDos[1]
    studentConFlechita = studentSinSeparar.split(",\n")
    for separaInicio in studentConFlechita:
        studentselect = separaInicio.split("< \"")
        sinFlechitaInicio = studentselect[1]
        separaNombre = sinFlechitaInicio.split("\" ; ")
        namestudent = separaNombre[0]
        quitaElFinal = separaNombre[1].split(" >")
        notaStudent = quitaElFinal[0]
        nuevoStudent = Estudiante(namestudent, float(notaStudent))
        students.append(nuevoStudent)#creo objetos estudiantes y ya tengo todos mis datos separados.
    print("********************************************************")
    print("Estudiante     Nota Obtenida")
    for estudiante in students:
        print(estudiante.nombre+" "+str(estudiante.calificacion))
    print("********************************************************")

    parameters = parameterSinSeparar.split(",")#separo mis parametros
    numberStudents = len(students)#obtengo el numero de estudiantes
    
    #Comienza el proceso de Orden
    
    ascendente = sorted(students, key=lambda Estudiante : Estudiante.calificacion)#los ordeno de forma ascendente

    descendente = sorted(students, key=lambda Estudiante : Estudiante.calificacion, reverse=True)#los ordeno de forma descendente

    notaMayorMemoria = max(students, key=lambda Estudiante : Estudiante.calificacion)#saco el alumno con mejor nota y lo paso a una variable
    notaMayor = (notaMayorMemoria.nombre)

    notaMenorMemoria = min(students, key=lambda Estudiante : Estudiante.calificacion)#saco el alumno con peor nota y lo paso a una variable
    notaMenor = (notaMenorMemoria.nombre)
    
    x=0
    for ss in students:#recorro la lista de estudiantes , paso su calificacion a una variable y la sumo
        yy = ss.calificacion
        x = x+yy
    promedio = str(round((x/numberStudents),2))#Divido la suma de notas entre el numero de estudiantes, lo redondeo y tengo el promedio


    gana=0#contador de ganadores
    for sg in students:#for que evaluara las notas arriba o igual a 61
        if sg.calificacion >= 61:
            gana = gana+1
            listaGanadores.append(sg)
    ganadores = str(gana)

    pierde=0
    for ty in students:#for que evalua las notas abajo de 61
        if ty.calificacion < 61:
            pierde = pierde+1
            listaPerdedores.append(ty)
    perdedores = str(pierde)

def generarRepo():
    global students
    global ascendente
    global descendente
    global parameters
    global listaGanadores
    global listaPerdedores
    global promedio
    global nameCurse
    global notaMayor
    global notaMenor
    global numberStudents
    global ganadores
    global perdedores
    print("********************************************************")
    print ("                                                                ")
    print("El curso se llama: "+nameCurse)
    print ("                                                                ")
    print("El curso tiene: "+str(numberStudents)+" estudiantes")
    print ("                                                                ")
    print("********************************************************")
    print ("                                                                ")
    print("El listado de estudiantes del curso como fue cargado.")
    print ("                                                                ")
    print("Estudiante    Nota Obtenida")
    print ("                                                                ")
    for jj in students:
        print(jj.nombre+" "+str(jj.calificacion))
    print ("                                                                ")
    print("********************************************************")
    print ("                                                                ")

    for para in parameters:
        if para == "ASC":
             print("********************************************************")
             print("El listado de estudiantes del curso de forma ascendente.")
             print ("                                                                ")
             print("Estudiante     Nota Obtenida")
             print ("                                                                ")
             for pp in ascendente:
                 print(pp.nombre+" "+str(pp.calificacion))
             print("********************************************************")
             print ("                                                                ")
             print ("                                                                ")
        if para == "DESC":
             print("********************************************************")
             print("El listado de estudiantes del curso de forma descendente.")
             print ("                                                                ")
             print("Estudiante     Nota Obtenida")
             print ("                                                                ")
             for oo in descendente:
                 print(oo.nombre+" "+str(oo.calificacion))
             print("********************************************************")
             print ("                                                                ")
             print ("                                                                ")
        if para == "AVG":
             print("********************************************************")
             print("El promedio de las notas del curso fue: "+promedio)
             print("********************************************************")
             print ("                                                                ")
             print ("                                                                ")
        if para == "MIN":
             print("********************************************************")
             print("El estudiante con la nota mas baja fue: ")
             print("Estudiante     Nota Obtenida")
             print(notaMenor)
             print("********************************************************")
             print ("                                                                ")
             print ("                                                                ")
        if para == "MAX":
             print("********************************************************")
             print("El estudiante con la nota mas alta fue: ")
             print("Estudiante     Nota Obtenida")
             print(notaMayor)
             print("********************************************************")
             print ("                                                                ")
             print ("                                                                ")
        if para == "APR":
             print("********************************************************")
             print("El número de estudiantes aprobados fue : "+ganadores +". Y son:")
             print ("                                                                ")
             print("Estudiante    Nota Obtenida")
             print ("                                                                ")
             for rr in listaGanadores:
                  print(rr.nombre+" "+str(rr.calificacion))
             print("********************************************************")
             print ("                                                                ")
             print ("                                                                ")
        if para == "REP":
             print("********************************************************")
             print("El número de estudiantes Reprobados fue : "+perdedores +". Y son:")
             print ("                                                                ")
             print("Estudiante    Nota Obtenida")
             print ("                                                                ")
             for dd in listaPerdedores:
                  print(dd.nombre+" "+str(dd.calificacion))
             print("********************************************************")
             print ("                                                                ")
             print ("                                                                ")

def generarRepoHTML():
    global students
    global ascendente
    global descendente
    global parameters
    global listaGanadores
    global listaPerdedores
    global promedio
    global nameCurse
    global notaMayor
    global notaMenor
    global numberStudents
    global ganadores
    global perdedores
    file = open("Reporte Notas.html", "w")
    head = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="reporte.css" type="text/css" />
                <title>Document</title>
                </head>
                <body>
                <h1><span class="yellow">NONBRE DEL CURSO: </span><span class="blue">&lt;</span>{nameCurse}<span class="blue">&gt;</span></h1>
                <h2>NUMERO DE ESTUDIANTES ASIGNADOS: <a target="_blank">{numberStudents}</a></h2>
                <h3>Listado como fue cargado.</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody>
                """
    file.write(head)
    for for1 in students:
        f1 = f"""
         <tr>
         <td>{for1.nombre}</td>
         <td>{for1.calificacion}</td>
         </tr>
         """
        file.write(f1)
    end1 = f"""
         </tbody>
         </table>
         """
    file.write(end1)
    for para in parameters:
        if para == "ASC":
            para1 = f"""
            <h3>Listado de forma ASCENDENTE.</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para1)
            for for2 in ascendente:
                f2 = f"""
                <tr>
                <td>{for2.nombre}</td>
                <td>{for2.calificacion}</td>
                </tr>
                """
                file.write(f2)
            end2 = f"""
             </tbody>
             </table>
             """
            file.write(end2)
        if para == "DESC":
            para2 = f"""
            <h3>Listado de forma DESCENDENTE.</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para2)
            for for3 in descendente:
                f3 = f"""
                <tr>
                <td>{for3.nombre}</td>
                <td>{for3.calificacion}</td>
                </tr>
                """
                file.write(f3)
            end3 = f"""
             </tbody>
             </table>
             """
            file.write(end3)
        if para == "AVG":
            para3 = f"""
            <h3>El PROMEDIO de notas del curso: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Promedio</td>
                 <td>{promedio}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para3)
        if para == "MIN":
            para4 = f"""
            <h3>El estudiante con la nota mas BAJA del curso fue: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Peor estudiante</td>
                 <td>{notaMenor}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para4)
        if para == "MAX":
            para5 = f"""
            <h3>El estudiante con la nota mas ALTA del curso fue: .</h3>
                <table class="container">
                 <tbody>
                 <tr>
                 <td>Mejor estudiante</td>
                 <td>{notaMayor}</td>
                 </tr>
                 </tbody>
                 </table>
            """
            file.write(para5)
        if para == "APR":
            para6 = f"""
            <h3>El numero de estudiantes aprobados fue: {ganadores}.</h3>
            <h3>Listado de estudiantes aprobados: .</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para6)
            for for3 in listaGanadores:
                f3 = f"""
                <tr>
                <td>{for3.nombre}</td>
                <td>{for3.calificacion}</td>
                </tr>
                """
                file.write(f3)
            end3 = f"""
             </tbody>
             </table>
             """
            file.write(end3)
        if para == "REP":
            para7 = f"""
            <h3>El numero de estudiantes reprobados fue: {perdedores}.</h3>
            <h3>Listado de estudiantes reprobados: .</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Nombe del Estudiante</h1>
                 </th>
                 <th>
                 <h1>Nota Obtenida</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody> 
            """
            file.write(para7)
            for for4 in listaPerdedores:
                f4 = f"""
                <tr>
                <td>{for4.nombre}</td>
                <td>{for4.calificacion}</td>
                </tr>
                """
                file.write(f4)
            end4 = f"""
             </tbody>
             </table>
             """
            file.write(end4)
    endd = f"""
         </body>
         </html>
         """
    file.write(endd)
    file.close()

while True:#Este while me ayuda a mantener activo el menu siempre
    menu()
    select = int(input("Selecciona alguna opción:"))

    if select == 1:
        separarpalabras()
    elif select == 2:
        generarRepo()
    elif select == 3:
        generarRepoHTML()
        print("Tu reporte ha sido generado con exito, buscalo en tus archivos")
    elif select == 4:
        print ("------          Gracias por usar mi programa :3           ------")
        print ("----------------------------------------------------------------")
        break
    else:
        print("No existe esa opción")