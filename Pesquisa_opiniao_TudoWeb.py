excelente = 0
bom = 0
ruim = 0

print("--- Pesquisa de Satisfação TudoWeb ---")

for i in range(1, 11):
    print(f"\nEntrevistado nº {i}")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    print("Opinião sobre o atendimento:")
    print("1: EXCELENTE | 2: BOM | 3: RUIM")
    opiniao = input("Sua resposta: ")

    if opiniao == "1":
        excelente += 1
    elif opiniao == "2":
        bom += 1
    elif opiniao == "3":
        ruim += 1
    else:
        print("Opção inválida! Esta resposta não será contabilizada.")

print("\n" + "="*30)
print("RESULTADO DA PESQUISA")
print("="*30)
print(f"Quantidade de respostas 'EXCELENTE': {excelente}")
print(f"Quantidade de respostas 'RUIM': {ruim}")
print(f"Total de entrevistados processados: {i}")