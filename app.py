from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'change-this-to-a-random-secret-key'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, 'bank.db')


# ── DB helpers ────────────────────────────────────────────────────────────────

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                name     TEXT    NOT NULL,
                cpf      TEXT    NOT NULL UNIQUE,
                email    TEXT    NOT NULL UNIQUE,
                password TEXT    NOT NULL,
                cred_lim REAL    DEFAULT 0.0,
                bal      REAL    DEFAULT 0.0
            )
        """)
        conn.commit()

def get_user(name):
    with get_connection() as conn:
        row = conn.execute(
            "SELECT id, name, bal, cred_lim FROM clients WHERE name = ?", (name,)
        ).fetchone()
    if row:
        return {'id': row[0], 'name': row[1], 'bal': row[2], 'cred_lim': row[3]}
    return None


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name     = request.form.get('name', '').strip()
        password = request.form.get('password', '').strip()
        with get_connection() as conn:
            row = conn.execute(
                "SELECT name FROM clients WHERE name = ? AND password = ?",
                (name, password)
            ).fetchone()
        if row:
            session['user'] = row[0]
            return redirect(url_for('dashboard'))
        else:
            flash('Nome ou senha incorretos.', 'error')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name     = request.form.get('name', '').strip()
        cpf      = request.form.get('cpf', '').strip()
        email    = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()

        with get_connection() as conn:
            cpf_exists   = conn.execute("SELECT 1 FROM clients WHERE cpf   = ?", (cpf,)).fetchone()
            email_exists = conn.execute("SELECT 1 FROM clients WHERE email = ?", (email,)).fetchone()

        if cpf_exists:
            flash('CPF já cadastrado.', 'error')
        elif email_exists:
            flash('Email já cadastrado.', 'error')
        else:
            with get_connection() as conn:
                conn.execute(
                    "INSERT INTO clients (name, cpf, email, password, cred_lim, bal) VALUES (?,?,?,?,?,?)",
                    (name, cpf, email, password, 0.0, 0.0)
                )
                conn.commit()
            flash('Conta criada com sucesso! Faça login.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    user = get_user(session['user'])
    return render_template('dashboard.html', user=user)


@app.route('/withdraw', methods=['POST'])
def withdraw():
    if 'user' not in session:
        return redirect(url_for('login'))
    try:
        amount = float(request.form.get('amount', 0))
    except ValueError:
        flash('Valor inválido.', 'error')
        return redirect(url_for('dashboard'))

    name = session['user']
    with get_connection() as conn:
        row = conn.execute("SELECT bal FROM clients WHERE name = ?", (name,)).fetchone()
        if row and amount <= row[0]:
            conn.execute("UPDATE clients SET bal = bal - ? WHERE name = ?", (amount, name))
            conn.commit()
            flash(f'Saque de R${amount:.2f} realizado com sucesso!', 'success')
        elif row and amount > row[0]:
            flash('Saldo insuficiente.', 'error')
        else:
            flash('Usuário não encontrado.', 'error')

    return redirect(url_for('dashboard'))


@app.route('/deposit', methods=['POST'])
def deposit():
    if 'user' not in session:
        return redirect(url_for('login'))
    try:
        amount = float(request.form.get('amount', 0))
    except ValueError:
        flash('Valor inválido.', 'error')
        return redirect(url_for('dashboard'))

    if amount <= 0:
        flash('O valor deve ser maior que zero.', 'error')
        return redirect(url_for('dashboard'))

    name = session['user']
    with get_connection() as conn:
        conn.execute("UPDATE clients SET bal = bal + ? WHERE name = ?", (amount, name))
        conn.commit()
    flash(f'Depósito de R${amount:.2f} realizado com sucesso!', 'success')
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    init_db()
    # host='0.0.0.0' makes the server reachable from any device on your LAN
    app.run(host='0.0.0.0', port=5000, debug=True)
