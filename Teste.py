score : int
salario : float
valorLiberado : float
taxaJuros : int
ValorSolicitado : float
Parcelas : int

salario = float(input("Digite sua renda: "))
score = int(input("Digite seu Score: "))
valorLiberado = salario * 35/100 * 12

print(f"Renda: {salario:.2f}")
print(f"Score: {score}")
print(f"Valor Máximo Liberado de Empréstimo: {valorLiberado:.2f}")
ValorSolicitado = int(input("Digite valor que deseja de Empréstimo: "))
Parcelas = int(input("Digite em quantas parcelas deseja pagar 1 até 12: "))








