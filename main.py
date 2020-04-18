from criptografar import criptografar ; from descriptografar import descriptografar ; import os ; from numerico import numerico
escolha = int(input("1 para criptografar e 2 para descriptografar: "))
os.system("clear")
print("@Gabriel Lopes - FEI")
print(" ")
if escolha == 1:
  criptografar()
elif escolha == 2:
  print("Para começar entenda a diferença: Método 1: utilizar uma word list para tentar descobrir a senha ; 2: utilizar um script para descobrir a senha de acordo com o tamanho de caracteres (apenas números)  ")
  print("")
  ver = int(input("1- Word List ; 2- Númerico: "))
  if ver == 1:
    descriptografar()
  elif ver == 2:
    numerico()
  else:
    print("Error")
else: 
  print("Error")
#Para descriptografar é necessário ter uma Word List, bastar salvar o txt como wordlist.txt
