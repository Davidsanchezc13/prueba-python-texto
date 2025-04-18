import re
import argparse
#declaro el argumentparser que me permitira recibir parametros desde la consola
parser=argparse.ArgumentParser(description="a script containing the procesar_texto function")
parser.add_argument("--text_path",help="path of the text")



def procesar_texto(texto):
  #utilizo una expresion regular para partir el string en substrings segun el requerimiento dado

  texto=re.split("[\.\,\s\(\)]",texto.lower())
  unique=set(texto)
  #elimino la cadena vacia
  unique.remove("")

  #inicializo variables que almacenaran el numero total de palabras,
  #el numero total de caracteres de la palabra mas larga,
  #la palabra mas larga y un formato de la forma palabra:#palabra en el texto
  totalw=0
  initialcharacters=0
  selectedword=""
  nwordsoutput=""
  #itero sobre el vocabulario del texto y saco las estadisticas requeridas
  for i in unique:
    wordcount=texto.count(i)
    totalw+=wordcount
    if len(i)>initialcharacters:
      initialcharacters=len(i)
      selectedword=i
    nwordsoutput+=f"{i}:{wordcount}, "

  return {"nwords": totalw,"unique_words": unique,"longest_word": selectedword,"number of matches":nwordsoutput}
  




  #obtengo los argumentos dados por el usuario y proceso el texto

args=parser.parse_args()

with open(args.text_path,"r") as f:
  texto=f.read()
  print(procesar_texto(texto))















