from calendar import c
from email.headerregistry import ContentDispositionHeader
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
  "tk_reser_double": "double",
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
contenido2 =""
contenido3 =""
contenido4 =""
fila=0
colum =0
tokenfinal = ""
patronfinal = ""
#se ignoran los comentarios para el analziador lexico

# busca si es un id o una palabra reservada    
def afd_Id(lexema2):
    global lexema,colum,contenido2,contenido3,contenido4
    if buscar_reservada(lexema2):
        #reporte1: guardar fila, columna,lexema, token y patron
        #reprote2: hacer un objeto para guarda estadop,caracter, lexema recono
        aux = colum
        aux = colum - len(lexema)
        print("Reconociod palabra reservada:",lexema2,"linea:",fila," columna:",aux, " token:",tokenfinal," patron:",patronfinal)#=======================
        #"<tr> <td>Linea</td>   <td>Columna</td>    <td>Lexema</td>  <td>Token</td>   <td>Patron</td>   </tr>"
        contenido2 += "<tr> <td>"+str(fila)+"</td><td>"+str(colum)+"</td>  <td>"+str(lexema2)+"</td>  <td>"+str(tokenfinal)+"</td>  <td>"+str(patronfinal)+"</td>   </tr>\n"  
    else:
        #hay que hacer aqui lo del reporte2
        aux = colum
        aux  = colum - len(lexema)
        print("Reconociod id:",lexema2," linea:",fila," columna:",aux, " token: tk_id","[a-zA-Z_][a-zA-Z0-9_]* ")#=======================
        contenido2 += "<tr> <td>"+str(fila)+"</td><td>"+str(colum)+"</td>  <td>"+str(lexema2)+"</td>  <td>"+"tk_id"+"</td>  <td>"+"[a-zA-Z_][a-zA-Z0-9_]* "+"</td>   </tr>\n"  
    lexema=""    

def buscar_reservada(char):
    global tokenfinal,patronfinal
    for token,patron in tokens.items():
        #print("toke:",token,"  patro:", patron)
        if patron == char:
            tokenfinal= token
            patronfinal = patron
            return True
    return False

#aqui se envia cada linea del archivo
def lee_Caracteres(cadena):
    global lexema,estado,fila,colum,contenido2,contenido4
    fila+=1
    colum = 0
    for char in cadena:
        
        #print("estado:",estado, "char:",char)
        if estado == 0:
            colum += 1
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
                #print("token reconocido",char)#=======================
                aux = colum
                aux = colum - len(lexema)
                print("token:",char,"linea:",fila," columna:",aux, " token:",tokenfinal," patron:",patronfinal)
                contenido2 += "<tr> <td>"+str(fila)+"</td><td>"+str(colum)+"</td>  <td>"+str(char)+"</td>  <td>"+str(tokenfinal)+"</td>  <td>"+str(patronfinal)+"</td>   </tr>\n"  
            else:
                print("char:",char)
                contenido4 += "<tr> <td>"+str(fila)+"</td><td>"+str(colum)+"</td>  <td>"+str(char)+"</td>  </tr>\n"  


        elif estado == 1:
            colum += 1
            if char == "/":
                estado = 2
            elif char == "*":
                estado =4

        elif estado == 2:
            colum += 1
            if char == "\n":
                print("termina el coment",estado)
                estado=0


        elif estado == 4:
            colum += 1
            if char == "*":
                estado =5

        elif estado == 5:
            colum += 1
            char =="/"
            print("coment varias")
            estado = 0
        
        elif estado == 7:
            colum += 1
            if char in digito:
                lexema += char
            elif char == ".":
                estado = 8
                lexema += char     
            elif char =="/":
                estado =1 
            elif buscar_reservada(char) or char == " " or char == "\n":
                estado =0
                #print("token num encontrado:", lexema)#=======================
                aux = colum
                aux = colum - len(lexema)
                print("token num:",lexema,"linea:",fila," columna:",aux, " token:",tokenfinal," patron:",patronfinal)
                contenido2 += "<tr> <td>"+str(fila)+"</td><td>"+str(colum)+"</td>  <td>"+str(lexema)+"</td>  <td>"+"tk_num"+"</td>  <td>"+"[0_9]*"+"</td>   </tr>\n"  
                lexema =""

        elif estado == 8:
            colum += 1
            if char in digito:
                estado = 7
                lexema += char
            elif buscar_reservada(char) or char == " ":
                estado = 0
                #print("token num decimal encontrado:", lexema)#=======================
                aux = colum
                aux = colum - len(lexema)
                print("Reconociod palabra reservada:",lexema,"linea:",fila," columna:",aux, " token:",tokenfinal," patron:",patronfinal)
                contenido2 += "<tr> <td>"+str(fila)+"</td><td>"+str(colum)+"</td>  <td>"+str(lexema)+"</td>  <td>"+"tk_decimal"+"</td>  <td>"+"[0_9]*.[0_9]*"+"</td>   </tr>\n"  
                lexema =""

        elif estado == 9:
            colum += 1
            if char in letra or char in digito or char =="_":
                lexema += char
            elif char == "/":
                estado =1
                afd_Id(lexema)
            elif buscar_reservada(char):
                #print("token encontrado_st9",char)#=======================
                aux = colum
                aux = colum - len(lexema)
                print("token:",char,"linea:",fila," columna:",aux, " token:",tokenfinal," patron:",patronfinal)
                contenido2 += "<tr> <td>"+str(fila)+"</td><td>"+str(colum)+"</td>  <td>"+str(char)+"</td>  <td>"+str(tokenfinal)+"</td>  <td>"+str(patronfinal)+"</td>   </tr>\n"  
                afd_Id(lexema)
                estado=0
            
            elif char in IGNORAR:
                estado = 0
                afd_Id(lexema)

        elif estado == 10:
            colum += 1
            if char != '"':
                lexema += char
            else:
                estado = 0
                lexema += char
                #print("token string",lexema)#=======================
                aux = colum
                aux = colum - len(lexema)
                print("token string:",lexema,"linea:",fila," columna:",aux, " token:",tokenfinal," patron:",patronfinal)
                contenido2 += "<tr> <td>"+str(fila)+"</td><td>"+str(colum)+"</td>  <td>"+str(lexema)+"</td>  <td>"+"tk_string"+"</td>  <td>"+"."+"</td>   </tr>\n"  
                lexema =""
        elif estado == 12:
            colum += 1
            if char in letra:
                estado = 13
                lexema += char
            else:
                estado = 0
        elif estado == 13:
            colum += 1
            if char == "'":
                estado = 0
                lexema += char
                #print("token char encontrado:",lexema)#=======================
                aux = colum
                aux = colum - len(lexema)
                print("token char:",lexema,"linea:",fila," columna:",aux, " token:",tokenfinal," patron:",patronfinal)
                contenido2 += "<tr> <td>"+str(fila)+"</td><td>"+str(colum)+"</td>  <td>"+str(lexema)+"</td>  <td>"+"tk_char"+"</td>  <td>"+"\"[a_z]\""+"</td>   </tr>\n"  
                lexema =""
        else:
            print("caracter invalido:",char)
            

            

def lecturaArchivo(ruta):     # validacion de la extension correcta  
    global fila,colum
    fila = 0
    colum = 0
    nombre_archivo, extension = os.path.splitext(ruta)
    if extension == ".sc":
        print("Ruta correcta")
        archivo = open(ruta, "r", encoding="utf-8")    
        for linea in archivo.readlines(): #separa con cada salto de linea           
            comp = linea.split()# comp se vuelve en un arreglo con cada linea
            if len(comp) == 0:  # valida si vienen una linea vacia                            
                print("aqui hay lineas en blanco xd")
            else:     
                linea = linea.lower()          
                lee_Caracteres(linea) 
            
                         
        archivo.close()
    else:
        print("la ruta ingresada es incorrecta")
    
    print("\nTotal lineas:",fila)
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

class Tokens:
    def __init__(self,fila,col,lexema,token,patron):
        self.fila=fila
        self.col=col
        self.lexema=lexema
        self.token= token
        self.patron = patron

class AFD:
    def __init__(self,estado,caracter,lexema,siguiente):
        self.estado = estado
        self.caracter = caracter
        self.lexema = lexema
        self.siguiente = siguiente

def Reporte1(nombre):
    contenido = "<!DOCTYPE html>\n"
    contenido +="<html lang=\"en\">\n"
    contenido += "<head>"
    contenido +="<meta charset=\"UTF-8\">"
    contenido +="<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">"
    contenido += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
    contenido +="<title>Document</title>"
    contenido +="</head>"
    contenido +="<body>"
    contenido += "<table  style=\"margin: 0 auto;\" class=\"default\">"
    contenido += "<tr> <td>Linea</td>   <td>Columna</td>    <td>Lexema</td>  <td>Token</td>   <td>Patron</td>   </tr>"
    contenido += contenido2
    contenido += " </table>"
    contenido += "<style>"
    contenido += "table,th,td{"
    contenido += "border: 1px solid black;"
    contenido += "}"
    contenido += "    th,td{"
    contenido += " padding: 5px;"
    contenido += "}"
    contenido += "</style>"
    contenido += "</body>"
    contenido += "</html>"


    archivo = open(nombre,'w')
    archivo.write(contenido)
    archivo.close()
    
def Reporte2(nombre):
    contenido = "<!DOCTYPE html>\n"
    contenido +="<html lang=\"en\">\n"
    contenido += "<head>"
    contenido +="<meta charset=\"UTF-8\">"
    contenido +="<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">"
    contenido += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
    contenido +="<title>Document</title>"
    contenido +="</head>"
    contenido +="<body>"
    contenido += "<table  style=\"margin: 0 auto;\" class=\"default\">"
    contenido += "<tr> <td>Linea</td>   <td>Columna</td>    <td>Lexema</td>  <td>Token</td>   <td>Patron</td>   </tr>"
    
    contenido += " </table>"
    contenido += "<style>"
    contenido += "table,th,td{"
    contenido += "border: 1px solid black;"
    contenido += "}"
    contenido += "    th,td{"
    contenido += " padding: 5px;"
    contenido += "}"
    contenido += "</style>"
    contenido += "</body>"
    contenido += "</html>"

    archivo = open(nombre,'w')
    archivo.write(contenido)
    archivo.close()

def Reporte3(nombre):
    contenido = "<!DOCTYPE html>\n"
    contenido +="<html lang=\"en\">\n"
    contenido += "<head>"
    contenido +="<meta charset=\"UTF-8\">"
    contenido +="<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">"
    contenido += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
    contenido +="<title>Document</title>"
    contenido +="</head>"
    contenido +="<body>"
    contenido += "<table  style=\"margin: 0 auto;\" class=\"defacult\">"
    contenido += "<tr> <td>Linea</td>   <td>Columna</td>    <td>Caracter</td> </tr> "
    contenido += contenido4
    contenido += " </table>"
    contenido += "<style>"
    contenido += "table,th,td{"
    contenido += "border: 1px solid black;"
    contenido += "}"
    contenido += "    th,td{"
    contenido += " padding: 5px;"
    contenido += "}"
    contenido += "</style>"
    contenido += "</body>"
    contenido += "</html>"

    archivo = open(nombre,'w')
    archivo.write(contenido)
    archivo.close()

#menu()

#Reporte1()
#Reporte2()
#Reporte3()


def main():
    op=0
    while op<6:
        print()
        print(" *** Menu **** ")
        print("1. Leer archivo")
        print("2. Generar reporte de tokens")
        print("3. Generar reporte de errores")
        print("4. Generar AFD")
        print("5. Salir")
        op=int(input("Ingrese su opcion: "))

        if (op==1):
           print()
           ruta = input("Ingrese una ruta: ")
           lecturaArchivo(ruta)
           #lecturaArchivo("C:/Users/otrop/Desktop/LFP-JV-201902689-P1/pruebita.sc")          

           
           
        elif(op==2):
            nombreHTML = input("Ingrese el nombre para el HTML: ")
            Reporte1(nombreHTML)
            
        elif(op==3):
            nombreHTML = input("Ingrese el nombre para el HTML: ")
            Reporte3(nombreHTML)
            
        elif(op==4):
            nombreHTML = input("Ingrese el nombre para el HTML: ")
            Reporte2(nombreHTML)
        elif(op==5):
            print(" ADIOS ")
            break
        else:
            print()
            print("ERROR. Ingrese una opción valida")
            return main()

if __name__ == '__main__':
    main();      
