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

def main():
    while True:
        print("\n Mini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar lead")
        print("[0] Sair do Programa")
        print("\n")

        opt = input("Escolha uma opção")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

def list_leads():
    leads = control.read_leads()
    print(leads)

# Validar se esse é o arquivo principal
if __name__ == "__main__":
    main()

