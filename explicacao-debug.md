# Análise de Erros - `debug.py`

## Erros Identificados

### Erro 1: String sem aspas
```python
item1 = float(input(Preço do item 1? ))
```
**Problema**: A string `"Preço do item 1?"` está sem aspas, causando `NameError`.  
**Correção**: Adicionar aspas: `input("Preço do item 1? ")`

---

### Erro 2: Tipo incorreto para desconto
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```
**Problema**: `input()` retorna uma **string**, mas está sendo usado em operação matemática (divisão).  
**Correção**: Converter para `float()`: `desconto_cupom = float(input(...))`

---

### Erro 3: String não formatada (f-string ausente)
```python
print(" Item 2:        R$ {total_item2:.2f}")
```
**Problema**: Falta o `f` antes das aspas para ativar a formatação. A variável não será substituída.  
**Correção**: `print(f" Item 2:        R$ {total_item2:.2f}")`

---

### Erro 4: Comparação com string
```python
if desconto_cupom > 0:
```
**Problema**: `desconto_cupom` é uma string, não pode ser comparada com número.  
**Correção**: Converter para `float` (conforme Erro 2).

---

### Erro 5: Indentação incorreta
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```
**Problema**: O `print` do desconto está fora do bloco `if` devido à indentação incorreta.  
**Correção**: Indentar com 4 espaços para ficar dentro do `if`.

---

## Resumo dos Erros

| Linha | Erro | Tipo |
|-------|------|------|
| 4 | String sem aspas | SyntaxError |
| 17-18 | String usada em operação matemática | TypeError |
| 29 | f-string ausente | NameError |
| 34 | Comparação string > número | TypeError |
| 35 | Indentação incorreta | Lógica |

---

## Código Corrigido

```python
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))  # ← Corrigido: aspas adicionadas

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))  # ← Corrigido: float()
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")  # ← Corrigido: f-string
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:  # ← Corrigido: comparação numérica
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")  # ← Corrigido: indentação

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```