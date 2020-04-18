def criptografar ():
  import os; import hashlib 
  palavra = input("Palavra: ")
  palavra=hashlib.md5(palavra.encode()) ;   palavra=palavra.hexdigest()
  os.system('clear')
  print("Crypt:",palavra)