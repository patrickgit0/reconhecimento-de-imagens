"""
Módulo para cálculo de estatísticas básicas de listas numéricas.
"""
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
        numeros: Lista de números para calcular estatísticas.
        
    Returns:
        NamedTuple contendo total, média, maior e menor valor.
        
    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not numeros:
        raise ValueError("A lista não pode estar vazia")
    
    total = sum(numeros)
    media = total / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    
    return Estatisticas(total=total, media=media, maior=maior, menor=menor)


def main() -> None:
    """Função principal para demonstrar uso do módulo."""
    numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    
    resultado = calcular_estatisticas(numeros)
    
    print(f"Total: {resultado.total}")
    print(f"Média: {resultado.media}")
    print(f"Maior: {resultado.maior}")
    print(f"Menor: {resultado.menor}")


if __name__ == "__main__":
    main()