from operator import truediv
import os

D = ["1","2","3","4","5","6","7","8","9","0"]
L= ["a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
reservada = ["void","int","string","double","char","boolean","if","else","while","do"]
tokens = {
  "tk_reser_void": "void",
  "tk_reser_int": "int",
  "tk_reser_string": "string",
  "tk_reser_double": "doble",
  "tk_reser_char": "char",
  "tk_reser_boolean": "boolean",
  "tk_reser_if": "if",
  "tk_reser_else": "else",
  "tk_reser_while": "while",
  "tk_reser_do": "do",
  "tk_puntocoma":";",

  "tk_parentesis_apertura":"(",
  "tk_parentesis_cierre":")",
  "tk_llave_apertura":"{",
  "tk_llave_cierre":"}",

  "tk_operador_suma": "+",
  "tk_operador_resta": "-",
  "tk_operador_multiplicacion": "*",
  "tk_operador_division": "/",
  "tk_operador_resto": "%",
  "tk_operador_igualacion": "==",
  "tk_operador_diferenciacion": "!=",
  "tk_operador_mayorigual":">=",
  "tk_operador_menorigual":"<=",
  "tk_operador_and":"&&",
  "tk_operador_or":"||",
  "tk_operador_asignacion": "=",
  "tk_operador_menor":"<",
  "tk_operador_mayor":">",
  "tk_operador_not":"!",
  "tk_punto":"."
}
lexema = ""
estado = 0
estado2 = 0
def afdComentarios(caracter):
    global estado
    if caracter == "/" and estado == 0:
        estado = 1
    elif estado == 1 and caracter == "/":
        estado = 2
    elif estado == 2 and caracter == "\n":
        print("termina el coment",estado)
        estado=0
    elif caracter == "*" and estado ==1:#varias lienas
        
        estado =4
    elif estado == 4 and caracter == "*":
        estado =5
    elif estado == 5 and caracter =="/":
        print("coment varias")
        estado = 0
    else:
        print("leyendo",estado)
    
def afd_Id(caracter):
    cont =1

def lee_Caracteres(cadena):
    for x in range(0,len(cadena)):
        print(cadena[x])
        if estado2 == 0:
            afdComentarios(cadena[x])
        elif estado2 ==1:
            afd_Id(cadena[x])
        elif estado2 ==2:
            afd_num(cadena[x])
        elif estado2 == 3:
            afd_reservadas(cadena[x])
            

def lecturaArchivo(ruta):     # validacion de la extension correcta  
    nombre_archivo, extension = os.path.splitext(ruta)
    line,columna = 0,0
    if extension == ".sc":
        print("Ruta correcta")
        archivo = open(ruta, "r", encoding="utf-8")    
        for linea in archivo.readlines(): #separa con cada salto de linea           
            comp = linea.split()# comp se vuelve en un arreglo con cada linea
            if len(comp) == 0:  # valida si vienen una linea vacia                            
                print("aqui hay lineas en blanco xd")
            else:
                
                print("tamos viendo kpx")               
                lee_Caracteres(linea) 
            line += 1
                         
        archivo.close()
    else:
        print("la ruta ingresada es incorrecta")
    
    print("\nTotal lineas:",line)
#C:/Users/otrop/Desktop/LFP-JV-201902689-P1/prueba.sc
#C:/Users/otrop/Desktop/LFP-JV-201902689-P1/pruebita.sc
#agregar caracteres que no estan disponibles en el lenguaje como @#$%
def menu():
    fin = True
    while fin:
        print("\n1.  Cargar Archivo    \n2. Generar grafico \n3. Salir \n")
        opc = input("Ingrese el número de la opción: ")
        if opc == "1":
            print("Ingrese la ruta del archivo")
            ruta = input() 
            lecturaArchivo(ruta)
        elif opc =="2":
            print("Generando reportes")
        elif opc =="3":
            fin = False

#menu()
lecturaArchivo("C:/Users/otrop/Desktop/LFP-JV-201902689-P1/pruebita.sc")