import pandas as pd
import functions as func
import config

main_df= pd.read_excel('excel_table.xlsx')
main_df.columns = ['name', 'id', 'cpf', 'email', 'password', 'cred_lim', 'bal']
amount=0

print("Bem-vindo ao sistema de gerenciamento de clientes!")

while True:
    name= input('Digite o nome do cliente: ')
    password= input('Digite a senha do cliente: ')
    check1= main_df.loc[main_df['name'] == name, 'password']

    if check1.empty:
        print("Nome ou senha incorretos.\nTente novamente.")
        continue

    if check1.values[0].astype(str) == password:
        user_row= main_df.loc[(main_df['name'] == name)]
        balance= user_row['bal'].values[0]
        break
    else:
        print("Nome ou senha incorretos.\nTente novamente.\n")

    
print(f"Bem-vindo, {name}! Seu saldo atual é: R${balance:.2f}")

action= input("Digite\nSacar: para realizar um saque\nDepositar: para realizar um depósito\n\n").strip().lower()

if action == 'sacar':
    func.withdraw(amount, balance, main_df, user_row, name)
elif action == 'depositar':
    func.deposit(amount, balance, main_df, user_row, name)
