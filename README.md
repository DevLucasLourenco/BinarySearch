# BinarySearch

A classe `BinarySearch` é responsável por realizar buscas binárias em uma lista ou tupla ordenada.

## Parâmetros

- `referencial` (lista ou tupla): O iterável onde será procurada a informação.
- `metodo` (string): Existem três opções disponíveis: 'find', 'count', 'locate'.

## Métodos

- `fetch(procura)`: Realiza a busca binária com o valor `procura` passado como parâmetro.

## Uso

```python
lista = [1, 5, 5, 5, 15, 17, 20, 24, 67, 76]
app = BinarySearch(referencial=lista, metodo='find')

x = app.fetch(5)
print(x)
