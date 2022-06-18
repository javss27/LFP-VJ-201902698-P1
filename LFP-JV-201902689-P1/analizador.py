from calendar import c
from operator import truediv
import os
from string import digits

#arreglos para buscar en los afd
digito = ["1","2","3","4","5","6","7","8","9","0"]
letra = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
IGNORAR = " \n\t"

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
  "tk_operador_not":"!"
  
  
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
        print("estado:",estado, "char:",char)
        if estado == 0:
            if char == "/":
                estado = 1
            elif char in digito:
                estado =7
                lexema += char
            elif char in letra or char == "_":
                estado = 9
                lexema +=char
            elif char in IGNORAR:
                print("ignorar espacio")
                estado = 0
            elif char == '"':
                estado =10
                lexema += char
            elif char == "'":
                estado = 12
                lexema += char
            elif buscar_reservada(char):
                print("token reconocido",char)
            else:
                print("char:",char)

        elif estado == 1:
            if char == "/":
                estado = 2
            elif char == "*":
                estado =4
        elif estado == 2:
            if char == "\n":
                print("termina el coment",estado)
                estado=0


        elif estado == 4:
            if char == "*":
                estado =5

        elif estado == 5:
            char =="/"
            print("coment varias")
            estado = 0
        
        elif estado == 7:
            if char in digito:
                lexema += char
            elif char == ".":
                estado = 8
                lexema += char      
            elif buscar_reservada(char) or char == " " or char == "\n":
                estado =0
                print("token num encontrado:", lexema)
                lexema =""

        elif estado == 8:
            if char in digito:
                estado = 7
                lexema += char
            elif buscar_reservada(char) or char == " ":
                estado = 0
                print("token num decimal encontrado:", lexema)
                lexema =""

        elif estado == 9:
            if char in letra or char in digito or char =="_":
                lexema += char
            elif buscar_reservada(char):
                print("token encontrado_st9",char)
                afd_Id(lexema)
                estado=0
            elif char in IGNORAR:
                estado = 0
                afd_Id(lexema)

        elif estado == 10:
            if char != '"':
                lexema += char
            else:
                estado = 0
                lexema += char
                print("token string",lexema)
                lexema =""
        elif estado == 12:
            if char in letra:
                estado = 13
                lexema += char
            else:
                estado = 0
        elif estado == 13:
            if char == "'":
                estado = 0
                lexema += char
                print("token char encontrado:",lexema)
                lexema =""
        else:
            print("caracter invalido:",char)




            

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
