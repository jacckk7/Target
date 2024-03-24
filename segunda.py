###############################################################################
#############################QUESTÃO DOIS######################################
###############################################################################

def is_fibonacci(numero):
  if numero == 0 or numero == 1:
    return True
  
  x = 0
  y = 1
  
  while y < numero:
    x, y = y, x + y

  if y == numero:
    return True
  else:
    return False

numero = int(input("Digite um número:\n"))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")