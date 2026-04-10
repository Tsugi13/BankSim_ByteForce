import pandas as pd
import functions as fn
import config as cfg

main_df= pd.read_excel(cfg.m_EXCEL_path)
main_df.columns = ['name', 'id', 'cpf', 'email', 'password', 'cred_lim', 'bal']

print("Bem-vindo ao sistema de gerenciamento de clientes!")
print("Login/Criação de conta?\n")
while True:
    if input("Digite 'Login' para acessar sua conta ou 'Criar' para criar uma nova conta: ").strip().lower() == 'criar':
        main_df = fn.create_account(main_df)
        fn.save_data(main_df)
        print("Agora, faça login para acessar sua conta.\n")
        continue
    else:
        name, balance, user_row = fn.login(main_df)
        if name and balance and user_row is not None:
            break
        else:
            continue

print(f"Bem-vindo, {name}! Seu saldo atual é: R${balance:.2f}")
while True:
    action= input("Digite:\nSacar: para realizar um saque\nDepositar: para realizar um depósito\nSair: para sair\n\n").strip().lower()

    if action == 'sacar':
        fn.withdraw(cfg.base_amount, balance, main_df, user_row, name)
        continue
    elif action == 'depositar':
        fn.deposit(cfg.base_amount, balance, main_df, user_row, name)
        continue
    elif action == 'sair':
        print("Obrigado por usar o sistema de gerenciamento de clientes. Até logo!")
        break