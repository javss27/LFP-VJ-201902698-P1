from calendar import c
from operator import truediv
import os
from string import digits

#arreglos para buscar en los afd
digito = ["1","2","3","4","5","6","7","8","9","0"]
letra = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
reservada = ["void","int","string","double","char","boolean","if","else","while","do"]

#diccionario para palabras y caracteres reservado
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
  "tk_punto":".",
  
}


lexema = ""
estado = 0
estado2 = 0
#se ignoran los comentarios para el analziador lexico
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

# busca si es un id o una palabra reservada    
def afd_Id(lexema2):
    global lexema
    if buscar_reservada(lexema2):
        #reporte1: guardar fila, columna,lexema, token y patron
        #reprote2: hacer un objeto para guarda estadop,caracter, lexema recono
        print("Reconociod palabra reservada:",lexema2)
    else:
        #hay que hacer aqui lo del reporte2
        print("Reconociod id:",lexema2)
    lexema=""    

"""def afd_char(lexema):

def afd_string(lexema):

def afd_num(lexema): """

def buscar_reservada(char):
    for token,patron in tokens.items():
        #print("toke:",token,"  patro:", patron)
        if patron == char:
            return True
    return False

#aqui se envia cada linea del archivo
def lee_Caracteres(cadena):
    global lexema,estado
    for char in cadena:
        print("estado:",estado)
        if char == "/" and estado == 0:
            estado = 1
        elif estado == 1 and char == "/":
            estado = 2
        elif estado == 2 and char == "\n":
            print("termina el coment",estado)
            estado=0
        elif char == "*" and estado ==1:#varias lienas           
            estado =4
        elif estado == 4 and char == "*":
            estado =5
        elif estado == 5 and char =="/":
            print("coment varias")
            estado = 0

        if estado == 0 and char in letra or char == "_":
            estado = 9
            lexema += char

        elif estado == 9:
            if char in letra or char in digito or char =="_":
                lexema += char
            elif buscar_reservada(char):
                estado = 10
                afd_Id(lexema)
        elif estado == 10:
            if char in letra or char in digito or char =="_" or char == " ":
                if char == " ":
                    continue
                else:
                    lexema += char
                    estado =9
            elif char == '"':
                estado =14
            elif char == "'":
                estado = 11
        elif estado == 14:
            if char == '"':
                estado == 15
                
            else:
                lexema += char
        elif estado == 11:
            if char in letra:
                estado = 12
        elif estado ==12:
            if char == "'":
                estado == 13

            #elif buscar_reservada(char):

        #elif estado == 0 and char in digits:




            

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
                
                #print("tamos viendo kpx")               
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
