# FarmTech Solutions - Projeto Completo

## Estrutura do pacote
- `app.py` -> aplicação em Python com menu, vetores, cálculos e exportação CSV
- `analise_agricola.R` -> análise estatística em R + API meteorológica pública
- `resumo_artigo.txt` -> resumo da disciplina de Formação Social
- `video_youtube.txt` -> arquivo para colar o link do vídeo no YouTube
- `dados_exemplo.csv` -> exemplo de arquivo exportado
- `roteiro_video.txt` -> roteiro simples de gravação do vídeo
- `README.md` -> instruções de uso

## Como executar

### 1) Rodar a aplicação em Python
No terminal:
```bash
python app.py
```

### 2) Inserir registros e exportar
No menu do sistema:
- escolha `1` para cadastrar dados
- escolha `5` para exportar os dados para `dados_agricolas.csv`

### 3) Rodar a análise em R
No R ou RStudio:
```r
source("analise_agricola.R", encoding = "UTF-8")
```

## Requisitos atendidos
- Duas culturas: Shitake e Horticultura
- Cálculo de área de plantio
- Cálculo de manejo de insumos
- Dados organizados em vetores
- Menu com entrada, saída, atualização, deleção e sair
- Uso de estruturas de repetição e decisão
- Estatística básica em R: média e desvio padrão
- Consumo de API meteorológica pública em R

## Sugestão de versionamento no GitHub
Branches:
- `main`
- `dev`
- `feature-python`
- `feature-r`
- `docs-resumo`

Exemplo de commits:
- `feat: cria menu principal em python`
- `feat: adiciona exportacao csv`
- `feat: cria analise estatistica em r`
- `docs: adiciona resumo do artigo`
