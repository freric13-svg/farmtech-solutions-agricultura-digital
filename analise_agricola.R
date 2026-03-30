# FarmTech Solutions - Análise em R
# Lê o CSV gerado pelo Python, calcula estatísticas básicas
# e consome uma API meteorológica pública (Open-Meteo).

options(encoding = "UTF-8")

if (!require(jsonlite)) {
  install.packages("jsonlite", repos = "https://cloud.r-project.org")
  library(jsonlite)
}

arquivo <- "dados_agricolas.csv"

if (!file.exists(arquivo)) {
  cat("Arquivo", arquivo, "não encontrado.\n")
  cat("Primeiro execute o app.py e exporte os dados para CSV.\n")
} else {
  dados <- read.csv2(arquivo, stringsAsFactors = FALSE)

  dados$area_m2 <- as.numeric(gsub(",", ".", dados$area_m2))
  dados$quantidade_total <- as.numeric(gsub(",", ".", dados$quantidade_total))
  dados$dosagem <- as.numeric(gsub(",", ".", dados$dosagem))

  cat("============================================\n")
  cat("FARMTECH SOLUTIONS - ANÁLISE ESTATÍSTICA\n")
  cat("============================================\n\n")

  cat("Total de registros:", nrow(dados), "\n")
  cat("Média da área (m²):", round(mean(dados$area_m2, na.rm = TRUE), 2), "\n")
  cat("Desvio padrão da área (m²):", round(sd(dados$area_m2, na.rm = TRUE), 2), "\n")
  cat("Média da quantidade total de insumos:", round(mean(dados$quantidade_total, na.rm = TRUE), 2), "\n")
  cat("Desvio padrão da quantidade total:", round(sd(dados$quantidade_total, na.rm = TRUE), 2), "\n\n")

  cat("Resumo por cultura:\n")
  culturas <- unique(dados$cultura)

  for (c in culturas) {
    sub <- dados[dados$cultura == c, ]
    cat("\nCultura:", c, "\n")
    cat("  Registros:", nrow(sub), "\n")
    cat("  Média de área:", round(mean(sub$area_m2, na.rm = TRUE), 2), "m²\n")
    cat("  Desvio da área:", round(sd(sub$area_m2, na.rm = TRUE), 2), "m²\n")
    cat("  Média de insumos:", round(mean(sub$quantidade_total, na.rm = TRUE), 2), "\n")
  }
}

cat("\n============================================\n")
cat("DADOS METEOROLÓGICOS - ITAPECERICA DA SERRA\n")
cat("============================================\n")

latitude <- -23.7169
longitude <- -46.8493

url <- paste0(
  "https://api.open-meteo.com/v1/forecast?",
  "latitude=", latitude,
  "&longitude=", longitude,
  "&current=temperature_2m,relative_humidity_2m,wind_speed_10m",
  "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum",
  "&timezone=America%2FSao_Paulo",
  "&forecast_days=3"
)

resposta <- fromJSON(url)

cat("\nCondições atuais:\n")
cat("Temperatura:", resposta$current$temperature_2m, resposta$current_units$temperature_2m, "\n")
cat("Umidade relativa:", resposta$current$relative_humidity_2m, resposta$current_units$relative_humidity_2m, "\n")
cat("Velocidade do vento:", resposta$current$wind_speed_10m, resposta$current_units$wind_speed_10m, "\n")

cat("\nPrevisão para os próximos dias:\n")
for (i in 1:length(resposta$daily$time)) {
  cat(
    resposta$daily$time[i], "-",
    "Máx:", resposta$daily$temperature_2m_max[i], resposta$daily_units$temperature_2m_max, "|",
    "Mín:", resposta$daily$temperature_2m_min[i], resposta$daily_units$temperature_2m_min, "|",
    "Chuva:", resposta$daily$precipitation_sum[i], resposta$daily_units$precipitation_sum, "\n"
  )
}
