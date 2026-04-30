# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

# Conversão para int pois quantidade deve ser número inteiro
qtd1 = int(input("Quantidade do item 1: "))
# Conversão para float pois preço pode ter casas decimais
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

# Soma geral dos itens antes de taxas
subtotal = total_item1 + total_item2 + total_item3

# Regra de negócio: imposto fixo de 10%
imposto = subtotal * 0.10

# DESCONTO
# Entrada convertida para float para permitir cálculo percentual
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))

# Desconto aplicado sobre o subtotal (antes do imposto)
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
# Ordem: soma subtotal + imposto - desconto
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)

print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")

print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

# Exibe desconto apenas se houver cupom válido (> 0)
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)

# Uso de round para evitar problemas de ponto flutuante na exibição final
print(f" TOTAL:         R$ {round(total, 2):.2f}")

print(linha)
