def withdraw(a, b, c, d, name):
    a= float(input("Digite o valor a ser sacado: "))
    if a > b:
        print("Saldo insuficiente para realizar o saque.")
    else:
        b -= a
        c.loc[d.index, 'bal'] = b
        print(f"Saque realizado com sucesso! Seu novo saldo é: R${b:.2f}")
        c.loc[(c['name'] == name), 'bal'] = b
        c.to_excel('excel_table.xlsx', index=False)

def deposit(a, b, c, d, name):
        a= float(input("Digite o valor a ser depositado: "))
        b += amount
        c.loc[d.index, 'bal'] = b
        print(f"Depósito realizado com sucesso! Seu novo saldo é: R${b:.2f}")
        c.loc[(c['name'] == name), 'bal'] = b
        c.to_excel('excel_table.xlsx', index=False)