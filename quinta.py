###############################################################################
#############################QUESTÃO CINCO#####################################
###############################################################################

frase = input("Escreva uma frase ou palavra para ser invertida:\n")
frase_invertida = ''

for i in range(len(frase)):
  frase_invertida = frase[i] + frase_invertida
  
print(frase_invertida)