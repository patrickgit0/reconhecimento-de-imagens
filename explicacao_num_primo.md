# Explicação Técnica - Módulo de Números Primos

## Visão Geral

Este módulo implementa a verificação de números primos seguindo princípios de **Clean Code**, com código legível, bem documentado e modularizado.

## Estrutura do Código

```python
import math

def eh_primo(n: int) -> bool:
    """Verifica se um número é primo."""
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    return _nao_tem_divisor_impar(n)

def _nao_tem_divisor_impar(n: int) -> bool:
    """Verifica se o número não possui divisores ímpares."""
    limite = math.isqrt(n)
    
    for divisor in range(3, limite + 1, 2):
        if n % divisor == 0:
            return False
    
    return True

def listar_primos(ate: int) -> list[int]:
    """Lista todos os números primos até um limite."""
    return [n for n in range(2, ate + 1) if eh_primo(n)]
```

## Princípios Clean Code Aplicados

### 1. Nomes Significativos
- `eh_primo` - nome claro que indica propósito
- `_nao_tem_divisor_impar` - função privada com nome descritivo
- `listar_primos` - indica ação de listagem

### 2. Tipagem Estática (Type Hints)
```python
def eh_primo(n: int) -> bool:
def listar_primos(ate: int) -> list[int]:
```
- Define explicitamente tipos de entrada e saída
- Melhora autocomplete e detecção de erros

### 3. Docstrings Completas
Cada função possui:
- Descrição do propósito
- Parâmetros com tipos
- Retorno esperado
- Exemplos de uso (formato doctest)

### 4. Funções Pequenas e Especializadas
- `eh_primo()` - lógica principal
- `_nao_tem_divisor_impar()` - detalhe de implementação (privada)
- `listar_primos()` - funcionalidade adicional

### 5. Early Returns
- Retorna imediatamente em casos triviais
- Evita aninhamento excessivo de condicionais

## Detalhamento das Funções

### `eh_primo(n: int) -> bool`

| Passo | Condição | Ação |
|-------|----------|------|
| 1 | `n < 2` | Retorna `False` (0 e 1 não são primos) |
| 2 | `n == 2` | Retorna `True` (único primo par) |
| 3 | `n % 2 == 0` | Retorna `False` (pares > 2 não são primos) |
| 4 | else | Chama verificação de divisores ímpares |

### `_nao_tem_divisor_impar(n: int) -> bool`

- Usa `math.isqrt(n)` para raiz quadrada inteira (mais preciso)
- Itera apenas por divisores ímpares
- Retorna `False` ao encontrar primeiro divisor
- Retorna `True` se nenhum divisor for encontrado

### `listar_primos(ate: int) -> list[int]`

- Usa list comprehension para criar lista
- Filtra números de 2 até `ate` usando `eh_primo()`

## Complexidade

| Função | Tempo | Espaço |
|--------|-------|--------|
| `eh_primo` | O(√n) | O(1) |
| `_nao_tem_divisor_impar` | O(√n) | O(1) |
| `listar_primos` | O(n√n) | O(n) |

## Exemplos de Execução

```python
>>> eh_primo(2)
True
>>> eh_primo(7)
True
>>> eh_primo(10)
False
>>> listar_primos(20)
[2, 3, 5, 7, 11, 13, 17, 19]
```

## Boas Práticas Demonstradas

1. **Docstrings no formato Google** - documentação padronizada
2. **Type hints** - segurança de tipos em tempo de desenvolvimento
3. **Funções puras** - sem efeitos colaterais
4. **Nomenclatura consistente** - verbos para ações, snake_case
5. **Modularização** - separação de responsabilidades
6. **Código autoexplicativo** - mínimo de comentários necessários