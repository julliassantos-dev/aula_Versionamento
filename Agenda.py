def carregar_agenda():
    agenda = []
    try:
        with open("agenda.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 3:
                    agenda.append({"nome": partes[0], "telefone": partes[1], "email": partes[2]})
    except FileNotFoundError:
        pass 
    return agenda

def salvar_agenda(agenda):
    with open("agenda.txt", "w", encoding="utf-8") as arquivo:
        for contato in agenda:
            # Substitui ponto e vírgula para não quebrar o arquivo
            nome = contato['nome'].replace(";", "")
            telefone = contato['telefone'].replace(";", "")
            email = contato['email'].replace(";", "")
            arquivo.write(f"{nome};{telefone};{email}\n")

def adicionar_contato(agenda):
    print("\n--- Novo Contato ---")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    
    if not nome or not telefone:
        print("Erro: Nome e Telefone são obrigatórios!")
        return agenda

    agenda.append({"nome": nome, "telefone": telefone, "email": email})
    salvar_agenda(agenda)
    print("Contato salvo com sucesso!")
    return agenda

def listar_contatos(agenda):
    print("\n--- Contatos Salvos ---")
    if not agenda:
        print("Nenhum contato salvo.")
    else:
        for i, contato in enumerate(agenda, 1):
            print(f"{i}. {contato['nome']} | Tel: {contato['telefone']} | E-mail: {contato['email']}")

def menu():
    agenda = carregar_agenda()
    while True:
        print("\n=== MENU AGENDA ===")
        print("1. Ver contatos")
        print("2. Adicionar contato")
        print("3. Sair")
        opcao = input("Escolha uma opção (1-3): ")
        
        if opcao == "1":
            listar_contatos(agenda)
        elif opcao == "2":
            agenda = adicionar_contato(agenda)
        elif opcao == "3":
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()