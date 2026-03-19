# 🌱 FarmTech Solutions - Agricultura Digital

Projeto acadêmico desenvolvido para a **FarmTech Solutions**, com foco em apoiar a migração de uma fazenda para a **Agricultura Digital**, utilizando **Python** e **R** para cadastro, cálculo, análise estatística e consulta de dados meteorológicos.

---

## 📌 Objetivo do Projeto

Desenvolver uma solução computacional para auxiliar no gerenciamento de duas culturas agrícolas:

- **Cogumelo Shitake**
- **Horticultura / Olericultura**

A aplicação foi criada para:

- calcular área de plantio;
- calcular manejo de insumos;
- armazenar os dados em vetores;
- permitir entrada, listagem, atualização e exclusão de dados;
- exportar dados para análise estatística em **R**;
- consultar uma **API meteorológica pública** para apoio à tomada de decisão.

---

## 🌾 Culturas Trabalhadas

### 🍄 Cogumelo Shitake
Itapecerica da Serra se destaca pelo cultivo de cogumelos, com produção e cursos voltados para essa atividade.  
No projeto, o cultivo de Shitake considera:

- ambiente controlado em **estufa ou barracão**;
- necessidade de **alta umidade relativa**;
- temperatura ideal entre **18°C e 25°C**;
- uso de irrigação/umidificação frequente para manter o microclima adequado.

### 🥬 Horticultura / Olericultura
A horticultura contempla a produção de hortaliças, legumes e frutas em pequena ou média escala.  
No projeto, considera-se:

- cultivo em canteiros ou áreas retangulares;
- áreas variando de pequenas hortas comerciais até produções maiores;
- uso de fertilizantes e pulverização como manejo principal.

---

## ⚙️ Funcionalidades do Sistema em Python

A aplicação em Python possui menu interativo no terminal com as seguintes opções:

- **Entrada de dados**
- **Saída/Listagem de dados**
- **Atualização de dados**
- **Deleção de dados**
- **Exportação para CSV**
- **Sair do programa**

Além disso, o sistema utiliza:

- **vetores** para armazenamento das informações;
- **estruturas de decisão** (`if`, `elif`, `else`);
- **estruturas de repetição** (`while`);
- cálculo automático de área e insumos.

---

## 📐 Cálculo de Área

### Shitake
A área de produção é calculada com base em uma estrutura retangular:

Área = largura × comprimento

Exemplo:
- largura = 5 m
- comprimento = 8 m
- área = **40 m²**

### Horticultura
A área de cultivo também é calculada com base em formato retangular:

Área = largura × comprimento

Exemplo:
- largura = 10 m
- comprimento = 28 m
- área = **280 m²**

---

## 🧪 Cálculo de Manejo de Insumos

### Shitake
Permite calcular:

- **Água por m²**
- **Substrato por m²**

Exemplo:
- área = 40 m²
- dosagem de água = 2,5 L/m²
- total = **100 litros**

### Horticultura
Permite calcular:

- **Fertilizante por m²**
- **Pulverização em mL por metro**

Exemplo de pulverização:
- 12 ruas
- 20 metros por rua
- 500 mL por metro

Cálculo:
- total em mL = 12 × 20 × 500 = 120000 mL
- total em litros = **120 L**

---

## 🗂️ Estrutura dos Dados

Os dados são armazenados em vetores paralelos:

- `culturas`
- `tipos_area`
- `larguras`
- `comprimentos`
- `areas_m2`
- `insumos`
- `dosagens`
- `quantidades_totais`
- `observacoes`

---

## 📊 Análise em R

Após a exportação do arquivo CSV pelo Python, a aplicação em **R** realiza:

- leitura do arquivo `dados_agricolas.csv`;
- cálculo da **média**;
- cálculo do **desvio padrão**;
- resumo por cultura;
- consulta à **API Open-Meteo**;
- exibição de dados climáticos no terminal.

### Dados meteorológicos consultados
- temperatura atual;
- umidade relativa;
- velocidade do vento;
- previsão dos próximos dias.

---

## 🧰 Tecnologias Utilizadas

- **Python 3**
- **R**
- **CSV**
- **API Open-Meteo**
- **GitHub** para versionamento

---

## 📁 Estrutura do Projeto

```bash
farmtech-solutions/
├── app.py
├── analise_agricola.R
├── README.md
├── resumo_artigo.txt
├── video_youtube.txt
└── dados_agricolas.csv
