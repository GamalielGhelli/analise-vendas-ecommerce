# Análise de Vendas de E-commerce

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar e demonstrar habilidades em **análise de dados com Python**. A partir de uma base fictícia de vendas de um e-commerce de produtos de tecnologia, são exploradas todas as etapas de um fluxo de análise: geração e organização dos dados, tratamento das informações, cálculo de indicadores e criação de visualizações.

As análises ajudam a responder perguntas de negócio, como quais produtos vendem mais, quais categorias geram maior receita, como o faturamento evolui ao longo do tempo e quais estados apresentam os melhores resultados. Por utilizar dados sintéticos, o projeto tem finalidade exclusivamente educacional e integra meu portfólio de estudos em Python e análise de dados.

## Base de dados

O arquivo `notebooks/vendas.csv` contém **3.000 registros**, com **15 produtos**, **10 categorias** e **8 unidades federativas** (AC, AL, AP, AM, BA, CE, DF e ES). O período simulado vai de **1º de janeiro de 2026 a 23 de agosto de 2027**.

Cada registro representa um pedido de um único produto e contém: `ID_pedido`, `Data_pedido`, `Nome_produto`, `Categoria`, `Preco_unitario`, `Quantidade`, `Id_cliente`, `Cidade` e `Estado`.

Os dados são sintéticos e foram criados exclusivamente para aprendizado; os resultados não representam uma empresa real.

## Análises realizadas

### 1. Geração das vendas fictícias

No notebook [01_geração_ficiticia.ipynb](notebooks/01_gera%C3%A7%C3%A3o_ficiticia.ipynb), foi criada uma função que sorteia produtos, clientes, quantidades e localidades. A geração distribui cinco registros por dia, com horários aleatórios e quantidades de 1 a 7 unidades por pedido. Mouse Vertical e Teclado Mecânico recebem uma variação de preço entre 90% e 100% do preço de referência.

A execução registrada gera 3.000 vendas e exporta o resultado para `vendas.csv`.

### 2. Exploração e produtos mais vendidos

No notebook [02_explorando_dados.ipynb](notebooks/02_explorando_dados.ipynb), foram realizadas:

- Leitura do CSV e conversão de `Data_pedido` para data e hora.
- Inspeção dos tipos e do preenchimento das colunas com `info()`.
- Criação de `Faturamento`, calculado por **preço unitário × quantidade**.
- Criação de `Status_Entrega`, com uma regra didática baseada no estado.
- Agrupamento por produto, soma das quantidades e seleção dos dez produtos mais vendidos, apresentados em um gráfico de barras horizontais.

O ranking considera **unidades vendidas**, e não faturamento ou número de pedidos. Na base atual, o **Mouse Vertical** lidera com **870 unidades**, seguido por **SSD NVMe 1 TB** e **Controle sem fio**, ambos com **864 unidades**.

### 3. Faturamento do e-commerce

No notebook [03_analises do_ecommerce.ipynb](notebooks/03_analises%20do_ecommerce.ipynb), foram criadas a coluna de mês (`Mes`) e a coluna de faturamento para três análises:

| Análise | Como foi feita | Visualização |
| --- | --- | --- |
| Evolução mensal | Soma do faturamento por ano e mês | Gráfico de linhas |
| Faturamento por estado | Soma por UF, em ordem decrescente | Gráfico de barras |
| Faturamento por categoria | Soma por categoria, em ordem decrescente | Gráfico de barras com eixo monetário em milhares |

## Principais resultados

Valores conferidos no CSV versionado no projeto:

| Indicador | Resultado |
| --- | --- |
| Pedidos | 3.000 |
| Unidades vendidas | 12.066 |
| Faturamento total | R$ 6.173.321,63 |
| Produto mais vendido em unidades | Mouse Vertical — 870 unidades |
| Mês com maior faturamento | Março de 2027 — R$ 376.608,14 |
| Estado com maior faturamento | Amazonas (AM) — R$ 826.591,94 |
| Categoria com maior faturamento | Hardware — R$ 2.218.069,20 |

Hardware representa aproximadamente **35,93% do faturamento total**. O resultado mostra como o ranking por receita complementa o ranking por quantidade: produtos de maior preço podem ter grande participação financeira mesmo sem liderar em unidades vendidas.

## Limitações e cuidados de interpretação

- A coluna `Cidade` armazena nomes de estados e do Distrito Federal, apesar do nome do campo.
- A regra de entrega classifica SP, RJ e MG como `Rápida`. Como essas UFs não fazem parte da base gerada, todos os registros recebem `Normal`. Isso não mede prazos reais de entrega.
- Agosto de 2027 termina no dia 23 na base e não deve ser comparado diretamente com meses completos sem considerar essa diferença.
- A geração não fixa sementes aleatórias para `random` e NumPy. Executar novamente o primeiro notebook sobrescreve o CSV e pode alterar os resultados acima.
- A análise calcula faturamento bruto dos registros; a base não contém custos, fretes, impostos ou devoluções para calcular lucro.

## Tecnologias

Python, Pandas, NumPy, Matplotlib e Seaborn para manipulação e visualização dos dados; Watermark para consulta das versões do ambiente. As dependências são declaradas no `pyproject.toml` e registradas no `uv.lock`.

## Estrutura do projeto

```text
analise-vendas-ecommerce/
├── notebooks/
│   ├── 01_geração_ficiticia.ipynb
│   ├── 02_explorando_dados.ipynb
│   ├── 03_analises do_ecommerce.ipynb
│   └── vendas.csv
├── src/pjt/
│   ├── ambiente.py
│   ├── graficos.py
│   └── tratamento.py
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

As análises estão implementadas nos notebooks. `ambiente.py` exibe as versões das bibliotecas; `graficos.py` e `tratamento.py` ainda estão vazios.

## Como executar

Requisitos: Git, [uv](https://docs.astral.sh/uv/) e Python **3.14.2 ou superior**, conforme o `pyproject.toml`. Para abrir os notebooks no VS Code, utilize as extensões Python e Jupyter.

```powershell
git clone git@github.com:GamalielGhelli/analise-vendas-ecommerce.git
cd analise-vendas-ecommerce
uv sync --locked
```

Abra um notebook no VS Code e selecione o interpretador da pasta `.venv` como kernel. Se precisar instalar o kernel nesse ambiente:

```powershell
uv pip install ipykernel
```

Execute as células de cima para baixo. Configure o diretório de execução dos notebooks como `notebooks`, pois a leitura e a gravação usam o caminho relativo `vendas.csv`.

Para reproduzir o fluxo completo, siga a ordem **01 → 02 → 03**. Para explorar os resultados do CSV atual, comece pelo notebook **02**, sem executar novamente a geração.

Como alternativa ao VS Code, inicie o JupyterLab diretamente na pasta dos notebooks:

```powershell
cd notebooks
uv run --with jupyterlab --with ipykernel jupyter lab
```

Para consultar as versões do ambiente, a partir da raiz do projeto:

```powershell
uv run python src/pjt/ambiente.py
```

Autor: **Gamaliel Ghelli**.
