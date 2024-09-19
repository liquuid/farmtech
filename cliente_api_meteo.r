# Script em R para coletar e exibir informações meteorológicas

# Carregar os pacotes necessários
if (!require(httr)) install.packages("httr", dependencies=TRUE)
if (!require(jsonlite)) install.packages("jsonlite", dependencies=TRUE)

library(httr)
library(jsonlite)

# Definir a localização (latitude e longitude)
# Você pode alterar estes valores para a localização desejada
latitude <- -23.5505   # São Paulo
longitude <- -46.6333

# Construir a URL da API
api_url <- paste0(
  "https://api.open-meteo.com/v1/forecast?",
  "latitude=", latitude,
  "&longitude=", longitude,
  "&current_weather=true",
  "&timezone=auto"
)

# Fazer a requisição GET para a API
response <- GET(api_url)

# Verificar se a requisição foi bem-sucedida
if (status_code(response) == 200) {
  # Converter o conteúdo para JSON
  data <- fromJSON(rawToChar(response$content))
  
  # Extrair os dados meteorológicos atuais
  current_weather <- data$current_weather
  
  # Processar e exibir as informações
  cat("Informações Meteorológicas para a Localização (",
      latitude, ", ", longitude, "):\n", sep = "")
  cat("--------------------------------------------\n")
  cat("Data e Hora: ", current_weather$time, "\n")
  cat("Temperatura: ", current_weather$temperature, "°C\n")
  cat("Velocidade do Vento: ", current_weather$windspeed, "km/h\n")
  cat("Direção do Vento: ", current_weather$winddirection, "°\n")
  cat("Condição Climática: ",
      switch(as.character(current_weather$weathercode),
             "0" = "Céu limpo",
             "1" = "Principalmente claro",
             "2" = "Parcialmente nublado",
             "3" = "Nublado",
             "45" = "Nevoeiro",
             "48" = "Nevoeiro depositante",
             "51" = "Garoa leve",
             "53" = "Garoa moderada",
             "55" = "Garoa densa",
             "56" = "Garoa congelante leve",
             "57" = "Garoa congelante densa",
             "61" = "Chuva leve",
             "63" = "Chuva moderada",
             "65" = "Chuva forte",
             "66" = "Chuva congelante leve",
             "67" = "Chuva congelante forte",
             "71" = "Neve leve",
             "73" = "Neve moderada",
             "75" = "Neve forte",
             "77" = "Grãos de neve",
             "80" = "Aguaceiros leves",
             "81" = "Aguaceiros moderados",
             "82" = "Aguaceiros violentos",
             "85" = "Neve leve",
             "86" = "Neve forte",
             "95" = "Tempestade",
             "96" = "Tempestade com granizo leve",
             "99" = "Tempestade com granizo forte",
             "Código desconhecido"),
      "\n")
  
} else {
  cat("Erro ao obter os dados meteorológicos. Status da requisição: ",
      status_code(response), "\n")
}

