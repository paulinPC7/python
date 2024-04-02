numero_macas = int(input("Digite o número de maçãs compradas: "))


if numero_macas < 12:
  preco_unitario = 0.30
else:
  preco_unitario = 0.25


valor_total = numero_macas * preco_unitario

print(f"O valor total da compra é de R$ {valor_total:.2f}")
