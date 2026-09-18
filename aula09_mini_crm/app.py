from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    status = input("Status do fluxo de vendas: ")

    # validar os dados
    # agora, preciso modelar os dados
    # para isso, vamos usar o módulo.py
    # preciso modelar os dados com um dict

    print(model_lead(name, email, status))

    # com os dados modelados... preciso enviar para o .json
    # vou usar o control para enviar o dicionario ao lead
    control.create_lead(model_lead(name, email, status))

    print("Lead adicionado (func)")

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possível exportar")
    else:
        print(f"Exportando para{path_csv}")

def main():
    while True:
        print("\n Mini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar lead")
        print("[3] Buscar (nome/e-mail)")
        print("[4] Exportar para CSV")
        print("[0] Sair do Programa")
        print("\n")

        opt = input("Escolha uma opção")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

def list_leads():
    leads = control.read_leads()


    print(f"## | {"Nome":<10} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]}")

def search_leads():
    query = input("Buscar por: ").strip()
    if not query:
        print("Consulta vazia")
        return

    # Com a query digitada (busca)...  preciso enviar para o control
    # o control irá comparar a query com os dados do leads.json
    # e irá retornar os dados da busca
    leads_found =  control.read_leads_search(query)

    print(f"## | {"Nome":<10} | E-mail")
    for i, lead in leads_found:
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]}")

def export_leads():
    print("leads exportados")

# Validar se esse é o arquivo principal
if __name__ == "__main__":
    main()



