<div align="center">

# MCEpy

![GitHub top language](https://img.shields.io/github/languages/top/MauricioPaivadaSilva/MCEpy) ![GitHub language count](https://img.shields.io/github/languages/count/MauricioPaivadaSilva/MCEpy) ![GitHub License](https://img.shields.io/github/license/MauricioPaivadaSilva/MCEpy) ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/MauricioPaivadaSilva/MCEpy/main) ![GitHub repo size](https://img.shields.io/github/repo-size/MauricioPaivadaSilva/MCEpy)

</div>

### Resultados dos testes

<div align="center">

| Tipo do teste | Resultado |
|---|---|
| Pytest | [![Resultados](https://github.com/MauricioPaivadaSilva/MCEpy/actions/workflows/pytest.yaml/badge.svg)](https://github.com/MauricioPaivadaSilva/MCEpy/actions/workflows/pytest.yaml) |

</div>

## Sobre a biblioteca
A presente biblioteca aprensenta-se em sua *versão 0.4.1* e tem como foco interpretar dados inseridos em formato de coordenadas e de strings, e desta forma gera os gráficos para representar os dados inseridos.

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
|Pytest | 8.0.0|

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
- [x] Apresentar mais de um gráfico em uma única tela;
- [x] Fazer a animação do ciclo trigonométrico;
- [x] Fazer a animação do gráfico da função senoidal.

## Resultados obtidos

Para a validação dos das funcionalidades implementadas na lib, são realizados testes em que é validadas as mensagens de erro, pois é importante saber exatamente o que está acontecemdo com no programa em caso de erro. Assim como é realizados testes que validam pixel a pixel da imagem dos gráficos gerados, garantindo a integridade da lib.

### Gráficos gerados

1. Gráfico de função senoidal

<img src="img/origin_sin.png" alt="Gráfico de função senoidal" width="400"/>

2. Ciclo Trigonométrico com vetor imaginário 2+2j

<img src="img/origin_vec_1.png" alt="Ciclo Trigonométrico com vetor imaginário" width="400"/>

3. Ciclo Trigonométrico com vetor imaginário -2-2j

<img src="img/origin_vec_2.png" alt="Ciclo Trigonométrico com vetor imaginário" width="400"/>

4. Ciclo Trigonométrico com vetor real 5

<img src="img/origin_vec_3.png" alt="Ciclo Trigonométrico com vetor real" width="400"/>

5. Ciclo Trigonométrico com vetor imaginário 10i

<img src="img/origin_vec_4.png" alt="Ciclo Trigonométrico com vetor imaginário" width="400"/>

## Formas de utilização

* Chmada da lib:

`from MCEpy import MCEpy as mc`

Lembrando que **todos** os dados devem ser inseridos como _str_. Assim como o parametro `None` **deve** ser mantido como segundo argumento, caso seja alterado, a lib irá trabalhar em modo de teste, gerando dados e salvando os mesmos.

Pode ser atribuido como valor imaginário tanto _i_ como _j_. E no caso dos gráficos animados, é necessário inserir _Hz_ após o valor, como no exemplo.

<div align="center">

|Exemplos de comandos que podem ser utilizados | Resumo da funcionalidade|
|---|---|
| `mc("x", None)` | Irá gerar um gráfico senoidal estático. |
| `mc("y", None)` | Irá gerar um gráfico senoidal estático. |
| `mc("5", None)` | Irá gerar um gráfico do ciclo trigonométrico estático, com vetor puramente real. |
| `mc("10i", None)` | Irá gerar um gráfico do ciclo trigonométrico estático, com vetor puramente imaginário. |
| `mc("2+3i", None)` | Irá gerar um gráfico do ciclo trigonométrico estático em que há o vetor qe indica a representação gráfica do número complexo. No caso, o vetor direcionará para o primeio quadrante.|
| `mc("-2-3i", None)`| Irá gerar um gráfico do ciclo trigonométrico estático em que há o vetor qe indica a representação gráfica do número complexo. No caso, o vetor direcionará para o terceiro quadrante. |
| `mc("60Hz", None)`| Ira gerar os gráficos animados que se adaptarão confome a frequência inserida. |

</div>

## Agradecimentos
.

.

.
