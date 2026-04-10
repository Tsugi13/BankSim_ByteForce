import pandas as pd
import config as cfg

def withdraw(a, b, c, d, name):#Função para realizar o saque
    a= float(input("Digite o valor a ser sacado: "))
    if a > b:
        print("Saldo insuficiente para realizar o saque.")
    else:
        b -= a
        c.loc[d.index, 'bal'] = b
        print(f"Saque realizado com sucesso! Seu novo saldo é: R${b:.2f}")
        c.loc[(c['name'] == name), 'bal'] = b
        c.to_excel(cfg.m_EXCEL_path, index=False)

def deposit(a, b, c, d, name):#Função para realizar o depósito
        a= float(input("Digite o valor a ser depositado: "))
        b += a
        c.loc[d.index, 'bal'] = b
        print(f"Depósito realizado com sucesso! Seu novo saldo é: R${b:.2f}")
        c.loc[(c['name'] == name), 'bal'] = b
        c.to_excel(cfg.m_EXCEL_path, index=False)

def login(main_df):#Função para realizar o login do cliente
    name= input('Digite o nome do cliente: ')
    password= input('Digite a senha do cliente: ')
    check1= main_df.loc[main_df['name'] == name, 'password']

    if check1.empty:
        print("Nome ou senha incorretos.\nTente novamente.")
        return None, None, None

    if str(check1.values[0]) == password:
        user_row= main_df.loc[(main_df['name'] == name)]
        balance= user_row['bal'].values[0]
        return name, balance, user_row
    else:
        print("Nome ou senha incorretos.\nTente novamente.\n")
        return None, None, None

def get_next_id(main_df):#Função para obter o próximo ID disponível
    if main_df.empty:
        return 1
    return int(main_df['id'].max()) + 1

def user_exists(main_df, cpf, email):#Função para verificar se o CPF ou email já existe no DataFrame
    cpf_exists = not main_df.loc[main_df['cpf'] == cpf].empty
    email_exists = not main_df.loc[main_df['email'] == email].empty
    return cpf_exists, email_exists

def create_account(df):#Função para criar uma nova conta de cliente
    print("\n=== Criar nova conta ===")

    while True:
        name = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        email = input("Email: ").strip()
        password = input("Senha: ").strip()

        cpf_exists, email_exists = user_exists(df, cpf, email)

        if cpf_exists:
            print("CPF já cadastrado.\n")
            continue

        if email_exists:
            print("Email já cadastrado.\n")
            continue

        new_id = get_next_id(df)

        new_user = {
            'id': new_id,
            'name': name,
            'cpf': cpf,
            'email': email,
            'password': password,
            'bal': 0.0
        }

        df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)

        print(f"\nConta criada com sucesso! ID do usuário: {new_id}\n")
        return df

def save_data(df):#Função para salvar os dados atualizados no arquivo Excel
    df.to_excel(cfg.m_EXCEL_path, index=False)