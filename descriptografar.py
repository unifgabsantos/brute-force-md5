def descriptografar():
  from time import sleep ; import os; import hashlib 
  crypt = input("Crypt: ") ;accountant=0 ;lista = []; lista_normal=[] ; arquivo = open("teste.txt","r")
  for x in arquivo.readlines():
    x=x.strip() ; x=hashlib.md5(x.encode()) ;   x=x.hexdigest() ;   lista.append(x)
  arquivo = open("teste.txt","r")
  for x in arquivo.readlines():
    lista_normal.append(x.strip())
  arquivo.close()
  for x in lista:
    accountant+=1
    if x == crypt:
      os.system('clear')
      print("Password Crack:",lista_normal[accountant-1])
      print("Attempt:", accountant)
      ver=1
      break
    else:
      os.system('clear')
      print("Password:",x)
      print("Attempt:", accountant)
      ver=0
  if ver == 0:
    os.system("clear")
    print("") ; print("") ; print("404 - Not Found ");print("");print("")