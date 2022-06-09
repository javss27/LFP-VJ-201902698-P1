import os
import re
simbst1 = "@#&^%$"
num = r"[0-9]"

reservada = ["void","int","string","double","char","boolean","if","else","while","do"]
def lecturaArchivo(ruta):     # validacion de la extension correcta   
    nombre_archivo, extension = os.path.splitext(ruta)
    if extension == ".sc":
        print("Ruta correcta")
        archivo = open(ruta, "r", encoding="utf-8")    
        for linea in archivo.readlines(): #separa con cada salto de linea 
                
            comp = linea.split()# comp se vuelve en un arreglo con cada linea
            if len(comp) == 0:  # valida si vienen una linea vacia                            
                print("aqui hay lineas en blanco xd")
            else:
                print("tamos viendo kpx")               
                #readCaractAfd(linea) 
                         
        archivo.close()
    else:
        print("la ruta ingresada es incorrecta")

#C:/Users/otrop/Desktop/LFP-JV-201902689-P1/prueba.sc
#C:/Users/otrop/Desktop/LFP-JV-201902689-P1/pruebita.sc
#agregar caracteres que no estan disponibles en el lenguaje como @#$%
def menu():
    fin = True
    while fin:
        print("\n1.  Cargar Archivo    \n2. Ingresar datos \n3. Salir \n")
        opc = input("Ingrese el número de la opción: ")
        if opc == "1":
            print("Ingrese la ruta del archivo")
            ruta = input() 
            lecturaArchivo(ruta)
        elif opc =="2":
            print("Generando reportes")
        elif opc =="3":
            fin = False

menu()