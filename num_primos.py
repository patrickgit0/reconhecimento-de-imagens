"""
Módulo para verificação de números primos.
"""
import math


def eh_primo(n: int) -> bool:
   """
    Verifica se um número inteiro é primo.

    Um número primo é aquele maior que 1 que possui exatamente dois divisores:
    1 e ele mesmo.

    A função aplica otimizações:
    - Elimina números menores que 2
    - Trata o caso especial do número 2
    - Descarta números pares maiores que 2
    - Verifica divisores ímpares até a raiz quadrada de n

    Args:
        n (int): Número inteiro a ser verificado.

    Returns:
        bool: 
            True se o número for primo.
            False caso contrário.

    Examples:
        >>> eh_primo(2)
        True
        >>> eh_primo(7)
        True
        >>> eh_primo(10)
        False
        >>> eh_primo(1)
        False
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    return _nao_tem_divisor_impar(n)


def _nao_tem_divisor_impar(n: int) -> bool:
    """
    Verifica se o número não possui divisores ímpares.
    
    Args:
        n: Número ímpar maior que 2.
        
    Returns:
        True se não houver divisor ímpar, False caso contrário.
    """
    limite = math.isqrt(n)
    
    for divisor in range(3, limite + 1, 2):
        if n % divisor == 0:
            return False
    
    return True


def listar_primos(ate: int) -> list[int]:
    """
    Lista todos os números primos até um limite.
    
    Args:
        ate: Limite superior (inclusivo).
        
    Returns:
        Lista de números primos.
    """
    return [n for n in range(2, ate + 1) if eh_primo(n)]


# Testes
if __name__ == "__main__":
    numeros = [1, 2, 7, 10, 17, 100]
    
    for num in numeros:
        resultado = "primo" if eh_primo(num) else "não primo"
        print(f"{num} é {resultado}")
    
    print(f"\nPrimos até 20: {listar_primos(20)}")
