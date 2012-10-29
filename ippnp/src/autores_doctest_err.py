def normaliza_autor(autor):
    """
    Normaliza o nome do autor.

    >>> normaliza_autor('Gustavo Fonseca')
    'FONSECA, Gustavo'
    """
    # separar as partes
    partes = autor.split()

    # alterar a caixa do ultimo elemento da lista
    partes[-1] = partes[-1].upper()

    # juntar as partes utilizando a virgula como separador
    autor_normalizado = ', '.join(partes)

    return autor_normalizado
