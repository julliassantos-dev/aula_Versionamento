# ===========
# calculadora
# ===========

def soma(a,b):
   return a + b

def subtracao(a,b):
   return a - b

def divisao(a,b):
   if b == 0:
      return "Div0"   
   else:
      return a / b
 
def multiplicacao(a,b): 
   return a * b

def exponent(a,b):
   return

while True: 
    print(" ===== Calculadora ===== ")
    print("1 - Soma ")
    print("2 - Subtração ")
    print("3 - Divisão ")
    print("4 - Multiplicação")
    print("0 - Sair")
    
    opcao = int(input("Escolha a operação desejada: "))

    if opcao == 0:
       break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if opcao == 1:
      resultado = soma(num1,num2) 
      
    elif opcao == 2:
      resultado = subtracao(num1,num2)
    
    elif opcao == 3:
      resultado = divisao(num1,num2)
    
    elif opcao == 4:
      resultado = multiplicacao(num1,num2)

    elif opcao = 5
    
    else :
       print("Opção inválida!")
       continue

    print(f"Resultado = {resultado}")
