score : int
salario : float
valorLiberado : float
taxaJuros : int
ValorSolicitado : float
Parcelas : int
ValorFinal : float

salario = float(input("Digite sua renda: "))
score = int(input("Digite seu Score: "))
valorLiberado = salario * 35/100 * 12

print(f"Renda: {salario:.2f}")
print(f"Score: {score}")
print("Informações:")
print(f"Valor Total a ser disponibilizado: {valorLiberado:.2f}")
ValorSolicitado = int(input("Digite valor que deseja de Empréstimo: "))
Parcelas = int(input("Digite em quantas parcelas deseja pagar *1 até 12*: "))

if score <= 533:
    taxaJuros = 9
elif score <= 766:
    taxaJuros = 7
else:
    taxaJuros = 3

ValorFinal = ValorSolicitado * (1 + taxaJuros/100) / Parcelas

print(f"Taxa de Juros: {taxaJuros} %")
print(f"{Parcelas} parcelas mensais de: R$ {ValorFinal:.2f}")













