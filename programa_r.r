vetores <- readLines("output.txt")

# Separar cada vetor
vetor1_str <- vetores[1]
vetor2_str <- vetores[2]

# Converter as strings em vetores numéricos
vetor1 <- as.numeric(unlist(strsplit(vetor1_str, ",")))
vetor2 <- as.numeric(unlist(strsplit(vetor2_str, ",")))

# Calcular a média e o desvio padrão do vetor 1
media1 <- mean(vetor1)
desvio1 <- sd(vetor1)

# Calcular a média e o desvio padrão do vetor 2
media2 <- mean(vetor2)
desvio2 <- sd(vetor2)

# Exibir os resultados
cat("Resultados para o Vetor 1:\n")
cat("Média:", media1, "\n")
cat("Desvio Padrão:", desvio1, "\n\n")

cat("Resultados para o Vetor 2:\n")
cat("Média:", media2, "\n")
cat("Desvio Padrão:", desvio2, "\n")

