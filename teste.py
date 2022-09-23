
salario = float(input("Digite sua renda: "))
score = int(input("Digite seu Score: "))
valorLiberado = salario * 35 / 100 * 12

if score < 300:
    print("Seu score é insuficiente para solicitar empréstimo")
elif score > 999:
    print("Valor de score inválido")
else:
    print("*" * 20)
    print("Informações:")
    print(f"Renda: R$ {salario:.2f}")
    print(f"Score: {score}")
    print(f"Valor Total a ser disponibilizado: R$ {valorLiberado:.2f}")
    print("*" * 20)

    ValorSolicitado = int(input("Digite valor que deseja de Empréstimo: "))
    while ValorSolicitado > valorLiberado:
        print("Valor solicitado maior que valor máximo disponibilizado")
        ValorSolicitado = int(input("Digite valor que deseja de Empréstimo: "))

    Parcelas = int(input("Digite em quantas parcelas deseja pagar (1 até 12): "))

    while Parcelas > 12 or Parcelas == 0:
        print("Número de parcelas deve ser entre 1 e 12")
        Parcelas = int(input("Digite em quantas parcelas deseja pagar (1 até 12): "))

    if score <= 533:
        taxaJuros = 9
    elif score <= 766:
        taxaJuros = 7
    else:
        taxaJuros = 3

    ValorFinal = ValorSolicitado * (1 + taxaJuros / 100) / Parcelas

    print(f"Taxa de Juros: {taxaJuros} %")
    print(f"{Parcelas} parcelas mensais de: R$ {ValorFinal:.2f}")

