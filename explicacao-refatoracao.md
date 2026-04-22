# Explicação do Código - `refatoracao.py`

## Visão Geral

O código calcula estatísticas básicas de uma lista de números: **total**, **média**, **maior** e **menor** valor.

## Análise do Código

```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn

x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

## Detalhamento da Função `c(l)`

### Parâmetros
- `l`: Lista de números

### Retorno
- `t`: Total (soma de todos os elementos)
- `m`: Média aritmética
- `mx`: Maior valor
- `mn`: Menor valor

### Passo a Passo

| Linha | Ação |
|-------|------|
| `t=0` | Inicializa acumulador da soma |
| Loop 1 | Soma todos os elementos em `t` |
| `m=t/len(l)` | Calcula a média |
| `mx=l[0]` | Inicializa maior com primeiro elemento |
| `mn=l[0]` | Inicializa menor com primeiro elemento |
| Loop 2 | Percorre lista atualizando maior e menor |
| `return t,m,mx,mn` | Retorna tupla com 4 valores |

## Problemas do Código (Refatoração Necessária)

1. **Nomes não descritivos**: `c`, `l`, `t`, `m`, `mx`, `mn` não indicam propósito
2. **Duplicação de lógica**: dois loops para iterar na lista
3. **Sem type hints**: não define tipos de entrada/saída
4. **Sem docstrings**: documentação ausente
5. **Função faz demais**: calcula 4 coisas diferentes

## Versão Refatorada Sugerida

```python
from typing import NamedTuple


class Estatisticas(NamedTuple):
    """Resultado do cálculo de estatísticas."""
    total: float
    media: float
    maior: float
    menor: float


def calcular_estatisticas(numeros: list[float]) -> Estatisticas:
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numeros: Lista de números.
        
    Returns:
        NamedTuple com total, média, maior e menor valor.
    """
    if not numeros:
        raise ValueError("Lista não pode estar vazia")
    
    total = sum(numeros)
    media = total / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    
    return Estatisticas(total=total, media=media, maior=maior, menor=menor)


# Uso
x = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
resultado = calcular_estatisticas(x)

print("total:", resultado.total)
print("media:", resultado.media)
print("maior:", resultado.maior)
print("menor:", resultado.menor)
```

## Resultado da Execução

```
total: 346
media: 34.6
maior: 89
menor: 2
```

## Boas Práticas Aplicadas na Refatoração

1. **Nomes significativos** - `calcular_estatisticas`, `numeros`, `estatisticas`
2. **Type hints** - `list[float]`, `Estatisticas`
3. **Docstrings** - documentação completa
4. **NamedTuple** - retorno estruturado e legível
5. **Funções built-in** - `sum()`, `max()`, `min()` para clareza
6. **Validação** - verifica lista vazia
7. **Princípio SRP** - função com responsabilidade única