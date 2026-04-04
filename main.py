import pandas as pd
import functions
import config

main_df= pd.read_excel('excel_table.xlsx', skiprows=0, header=1)
main_df.columns = ['name', 'id', 'cpf', 'email', 'password', 'cred_lim', 'bal']

print("Bem-vindo ao sistema de gerenciamento de clientes!")
name= input('Digite o nome do cliente: ')
password= input('Digite a senha do cliente: ')

name_exists= not main_df[main_df['name'] == name].empty
password_matches= not main_df[(main_df['name'] == name) & (main_df['password'] == password)].empty

if name_exists and password_matches:
    user_row= main_df.loc[(main_df['name'] == name) & (main_df['password'] == password)]
    balance= user_row['bal'].values[0]
    print(f"Bem-vindo, {name}! Seu saldo atual é: R${balance:.2f}")

    action= input("Digite 'sacar' para realizar um saque ou 'depositar' para realizar um depósito: ").strip().lower()

    if action == 'sacar':
        amount= float(input("Digite o valor a ser sacado: "))
        if amount > balance:
            print("Saldo insuficiente para realizar o saque.")
        else:
            balance -= amount
            main_df.loc[user_row.index, 'bal'] = balance
            print(f"Saque realizado com sucesso! Seu novo saldo é: R${balance:.2f}")
        main_df.loc[(main_df['name'] == name) & (main_df['password'] == password), 'bal'] = balance
        main_df.to_excel('excel_table.xlsx', index=False)

    elif action == 'depositar':
        amount= float(input("Digite o valor a ser depositado: "))
        balance += amount
        main_df.loc[user_row.index, 'bal'] = balance
        print(f"Depósito realizado com sucesso! Seu novo saldo é: R${balance:.2f}")
        main_df.loc[(main_df['name'] == name) & (main_df['password'] == password), 'bal'] = balance
        main_df.to_excel('excel_table.xlsx', index=False)
else:
    if not name_exists:
        print("Nome não encontrado.")
    elif not password_matches:
        print("Senha incorreta.")