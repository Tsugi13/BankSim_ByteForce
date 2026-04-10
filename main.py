import pandas as pd
import functions as fn
import config as cfg

main_df= pd.read_excel('excel_table.xlsx')
main_df.columns = ['name', 'id', 'cpf', 'email', 'password', 'cred_lim', 'bal']
amount=0

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
        break
    
print(f"Bem-vindo, {name}! Seu saldo atual é: R${balance:.2f}")

action= input("Digite:\n\nSacar: para realizar um saque\nDepositar: para realizar um depósito\n\n").strip().lower()

if action == 'sacar':
    fn.withdraw(amount, balance, main_df, user_row, name)
elif action == 'depositar':
    fn.deposit(amount, balance, main_df, user_row, name)
