#Calculadora Python

val1 = int(input("Digite o primero número: "))
val2 = int(input("Digite o segundo número: "))
print("-> Soma: +")
print("-> subtração: -")
print("-> Multiplicação: *")
print("-> divisão: /")
operacao = input("Informe a Operação com os sinais a cima: ")
resultado = 0

#Operação
if(operacao == '+'):
  resultado = val1 + val2
elif(operacao == '-'):
  resultado = val1 - val2
elif(operacao == '*'):
  resultado = val1 * val2
elif(operacao == '/'):
  resultado = val1 / val2
else:
  print(":( Houve algum erro! Reinicie o programa.")
  
print(val1,operacao,val2,'=',resultado)