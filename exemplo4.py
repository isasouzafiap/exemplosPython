valor = input (" Digite numero : ")
numA = float ( valor )
op = input (" Operador (+ -*/) : ")
valor = input (" Digite numero : ")
numB = float ( valor )

if op == "+":
    resultado = numA + numB
    #usando o elif apos passar peloverdadeiro ele ignorario o restp
elif op == "-":
    resultado = numA - numB
elif op == "*":
    resultado = numA * numB
elif op == "/":
    resultado = numA / numB
    
print (f"Resposta: {resultado}")