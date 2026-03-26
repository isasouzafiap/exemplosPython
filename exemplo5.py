ms1 = float(input("Média 1 semestre: "))
ms2 = float(input("Média 2 semestre: "))

ministrados = int(input("Qtd aulas ministradas: "))
assistidos = int (input("Qtd aulas assistidas"))

media_final = (4 * ms1 + 6 * ms2) /10
presenca_percent = assistidos / ministrados

if presenca_percent >= 0.7:
    if media_final >= 6:
        print(f"Aprovado MF: {media_final}")
    elif media_final >= 4:
        print(f"Vc está de Exame e precisa de: {12 - media_final}")
    else:
        print(f"Vc foi reprovado, média {media_final}")
else:    
        print(f"Reprovado por faltar {presenca_percent * 100}%")