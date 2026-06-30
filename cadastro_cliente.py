#Horizon Bank - Sistema de Atendimento Terminal
#Sa1 - Situação de Aprendizagem 
"""
FASE 1 - visual
Cria uma banner com HORIZON BANK + frase -  BASE trabalho de UI / UX
cria um menu de cadastro 
ciar um exibição de rodapé 

FASE 2 - fucionamento 
definir dados simular um banco de dados - informação ficara no topo garantir que o teste do professor,
será controlado. 

FASE 3

"""


# 1. BANCO DE DADOS (Lista de Listas: [CPF, Nome, Saldo])
clientes = [
    ["1", "Carlos Silva", 1500.0],
    ["2", "Ana Souza", 350.0]
]

# 2. SEU VISUAL
def exibicao_banner():
    print("====================================================")
    print("              HORIZON BANK              ")
    print(" Um banco que está com você em todos os momentos.")
    print("====================================================")

def exibicao_rodape():
    print("====================================================")
    print(" Horizon Bank 2026 | Transparencia | Carreira | SAC ")
    print("====================================================")

# 3. LÓGICA DO SISTEMA
def abrir_conta():
    print("\n--- ABRIR CONTA ---")
    cpf = input("Digite seu CPF: ").strip()
    nome = input("Digite seu nome: ").strip()
    
    # Salva apenas CPF, Nome e Saldo Inicial (0.0)
    clientes.append([cpf, nome, 0.0])
    print(f"[✓] Conta criada para {nome}!")

def mostrar_saldo(cliente):
    print(f"\n========================================")
    print(f" Bem-vindo(a), {cliente[1]}!")
    print(f" SEU SALDO ATUAL: R$ {cliente[2]:.2f}")
    print(f"========================================")
    
    print("1 - Fazer um Depósito\n2 - Voltar ao Menu")
    opcao = input("Escolha: ")
    
    if opcao == "1":
        valor = float(input("Valor do depósito: R$ "))
        cliente[2] += valor  # Soma direto no saldo (índice 2)
        print(f"[✓] Depósito realizado! Novo saldo: R$ {cliente[2]:.2f}")

def menu_principal():
    while True:
        exibicao_banner()
        print("1 - Acessar Conta (Login por CPF)\n2 - Abrir Nova Conta\n3 - Sair")
        exibicao_rodape()
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            cpf = input("Digite seu CPF: ")
            
            # Busca simples pelo CPF
            encontrado = None
            for c in clientes:
                if c[0] == cpf:
                    encontrado = c
            
            if encontrado:
                mostrar_saldo(encontrado)
            else:
                print("[!] CPF não encontrado.")
                
        elif opcao == "2":
            abrir_conta()
        elif opcao == "3":
            print("Até logo!")
            break
            
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    menu_principal()