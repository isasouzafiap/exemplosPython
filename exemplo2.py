placarA = int(input("Gols do time A: "))
palcarB = int(input("Gols do time B: "))

#decidindo resultado
if placarA == palcarB:
    print("Empate")
elif placarA > palcarB:
    print("Vencedor time A")

else:
    print("Vencedor Time B ")
print("fim de jogo")
