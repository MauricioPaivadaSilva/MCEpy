<div align="center">
<h1>MCEpy</h1>

![GitHub top language](https://img.shields.io/github/languages/top/MauricioPaivadaSilva/MCEpy) ![GitHub language count](https://img.shields.io/github/languages/count/MauricioPaivadaSilva/MCEpy) ![GitHub License](https://img.shields.io/github/license/MauricioPaivadaSilva/MCEpy) ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/MauricioPaivadaSilva/MCEpy/main) ![GitHub repo size](https://img.shields.io/github/repo-size/MauricioPaivadaSilva/MCEpy)

</div>

## Sobre a biblioteca
A presente biblioteca interpreta dados inseridos em formato de coordenadas e de strings, e desta forma gera os gráficos para representar os dados inseridos.

## Motivação

O presente projeto tem como motivação o trabalho desenvolvido pelo LABin - Labratório de educação inclusiva, que tem como intuito o a pesquisa-ação na área do ensino inclusivo.

## Sumário
* [Requisitos e forma de instalação](#requisitos-e-forma-de-instalação)
* [Funcionalidades esperadas](#funcionalidades-esperadas)
* [Resultados obtidos](#resultados-obtidos)
* [Formas de utilização](#formas-de-utilização)
* [Agradecimentos](#agradecimentos)
## Requisitos e forma de instalação


### Requisitos
<div align="center">

|Dependencia | Versão|
|---|---|
|Python | 3.12.0|
|pip | 23.3.2|
|Numpy | 1.26.3|
|Matplotlib | 3.8.2|

</div>

### Forma de Instalação

* Para instalar usando o setup.py: 

`pip install .`

* Para instalar usando o requirements.txt:

`pip install -r requirements.txt`

## Funcionalidades esperadas

- [x] Receber dados de valores puramente reais;
- [x] Receber dados de números complexos;
- [x] Gerar o gráfico de função senoidal;
- [x] Gerar o ciclo trigonométrico;
- [x] Gerar o vetor dentro do ciclo trigonométrico;
- [ ] Apresentar mais de um gráfico em uma única tela;
- [ ] Fazer a animação do ciclo trigonométrico;
- [ ] Fazer a animação do segundo gráfico.

## Resultados obtidos
. . . 

## Formas de utilização

* Chmada da lib:

`from MCEpy import Tratamento as tr`

<div align="center">

|Comando | Dados a serem inseridos | Resumo da funcionalidade|
|---|---|---|
| `tr.Complex()` | Exemplo de valore: `"2+3i"` ou `"2+3j"`. Também pode ser inserido `"x"` ou `"y"`. Lembrando que todas os dados devem ser inseridos como _str_. | Direciona os dados para seu tratamento. Os dados podem ser interpretados como um vetor complexo, valor puramente real ou puramente imaginário. Ao inserir os dados como complexo ele retornará um [vetor](), já se for inserido _x_ ou _y_ retornará um gráfico [senoidal]().
</div>

## Agradecimentos
.

.

.
