def menu():
    print("\n=== Menu Principal ===")
    print("1. Entrada de dados")
    print("2. Saída de dados")
    print("3. Editar dados")
    print("4. Deletar dados")
    print("5. Sair")

    opcao = input("Selecione uma opção: ")
    return opcao

def entrada_dados():
    print(f"\n--- Entrada de dados para a Cultura de Cana de Açucar ---\n")
    cana_dados[0] = float(input("Digite o comprimento em metros: "))
    cana_dados[1] = float(input("Digite a largura em metros: "))
    cana_dados[2] = float(input("Quantidade de Nitrogênio por m²: "))
    cana_dados[3] = float(input("Quantidade de Fósforo por m²: "))
    cana_dados[4] = float(input("Quantidade de Potássio por m²: "))
    print()
    print(f"\n--- Entrada de dados para a Cultura Laranja ---\n")
    laranja_dados[0] = float(input("Digite o comprimento em metros: "))
    laranja_dados[1] = float(input("Digite a largura em metros: "))
    laranja_dados[2] = float(input("Quantidade de Nitrogênio por m²: "))
    laranja_dados[3] = float(input("Quantidade de Fósforo por m²: "))
    laranja_dados[4] = float(input("Quantidade de Potássio por m²: "))
    
    print("\nDados inseridos com sucesso!")

def saida_dados():
    print("\n*** cana *** ")
    print(f"{'Comprimento (m):':<20} {cana_dados[0]:^10}")
    print(f"{'Largura (m):':<20} {cana_dados[1]:^10}")
    print(f"{'Nitrogênio por m²:':<20} {cana_dados[2]:^10} total necessário: {cana_dados[2]*cana_dados[0]*cana_dados[1]}")
    print(f"{'Fósforo por m²:':<20} {cana_dados[3]:^10} total necessário: {cana_dados[3]*cana_dados[0]*cana_dados[1]}")
    print(f"{'Potássio por m²:':<20} {cana_dados[4]:^10} total necessário: {cana_dados[4]*cana_dados[0]*cana_dados[1]}")
    print("")
    print("*** laranja *** ")
    print(f"{'Comprimento (m):':<20} {laranja_dados[0]:^10}")
    print(f"{'Largura (m):':<20} {laranja_dados[1]:^10}")
    print(f"{'Nitrogênio por m²:':<20} {laranja_dados[2]:^10} total necessário: {laranja_dados[2]*laranja_dados[0]*laranja_dados[1]}")
    print(f"{'Fósforo por m²:':<20} {laranja_dados[3]:^10} total necessário: {laranja_dados[3]*laranja_dados[0]*laranja_dados[1]}")
    print(f"{'Potássio por m²:':<20} {laranja_dados[4]:^10} total necessário: {laranja_dados[4]*laranja_dados[0]*laranja_dados[1]}")

def editar_dados():
    cultura_num = int(input("Qual cultura deseja editar? (1 - Cana ou 2 - Laranja): "))
    if cultura_num == 1:
        temp = cana_dados
        print(f"\nEditando dados da Cultura de Cana de Açucar")
    elif cultura_num == 2:
        temp = laranja_dados
        print(f"\nEditando dados da Cultura de Laranja")
    else:
        return
    
   

    print("1. Comprimento")
    print("2. Largura")
    print("3. Nitrogênio")
    print("4. Fósforo")
    print("5. Potássio")

    campo = int(input("Selecione o número do campo que deseja editar: ")) - 1
    temp[campo] = float(input("Digite o novo valor: "))
    print("Dados atualizados com sucesso!")

def deletar_dados():
    cultura_num = int(input("Qual cultura deseja editar? (1 - Cana ou 2 - Laranja): "))
    
    if cultura_num == 1:
        for i in range(5):
            cana_dados[i] = 0.0
        print(f"\nDados da Cultura de Cana de Açucar deletados com sucesso.")
    elif cultura_num == 2:
        for i in range(5):
            laranja_dados[i] = 0.0
        print(f"\nDados da Cultura de Laranja deletados com sucesso.")
    else:
        return

def main():
    while True:
        opcao = menu()
        if opcao == '1':
            entrada_dados()
        elif opcao == '2':
            saida_dados()
        elif opcao == '3':
            editar_dados()
        elif opcao == '4':
            deletar_dados()
        elif opcao == '5':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    cana_dados = [0.0, 0.0, 0.0, 0.0, 0.0] 
    laranja_dados = [0.0, 0.0, 0.0, 0.0, 0.0]
    main()