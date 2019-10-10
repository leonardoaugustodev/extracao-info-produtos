# Scripts temporários

## Requisitos
- Python 3
- Pipenv
- MongoDB

## Instalação
- Instalar todas as dependências com o **pipenv**

```
$ pipenv install
```

- Configurar os parâmetros do arquivo **.env**

- Rodar o script

```sh
$ pipenv run python3 src/app/ExtracaoProdutos/index.py
```

## Scripts
### Extração de informações de produtos (ExtracaoProdutos)
Script para extração das informações dos produtos a partir dos arquivos .doc e .docx contidos na pasta **Dados**.

### Calcular transportadora mais barata (CustoFrete)
Script que faz o cálculo da transportadora mais barata para uma lista de pedidos.

