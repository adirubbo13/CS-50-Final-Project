from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import pandas as pd

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('Databased.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        conn = get_db_connection()
        conn.execute('INSERT INTO USERS (FirstName, LastName) VALUES (?, ?)', (first_name, last_name))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        last_name = request.form['last_name']
        conn = get_db_connection()
        query = "SELECT * FROM ROUNDS WHERE LastName = ?"
        df = pd.read_sql_query(query, conn, params=(last_name,))
        conn.close()
        if not df.empty:
            df['front_nine_score'] = df.loc[:, 'Hole1':'Hole9'].sum(axis=1)
            df['back_nine_score'] = df.loc[:, 'Hole10':'Hole18'].sum(axis=1)
            df['total_score'] = df.loc[:, 'Hole1':'Hole18'].sum(axis=1)
            rounds = df.to_dict(orient='records')
        else:
            rounds = []
        return render_template('login.html', rounds=rounds)
    return render_template('login.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        last_name = request.form['last_name']
        date = request.form['date']
        scores = [request.form[f'hole{i}'] for i in range(1, 19)]
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO ROUNDS (Date, LastName, Hole1, Hole2, Hole3, Hole4, Hole5, Hole6, Hole7, Hole8, Hole9, Hole10, Hole11, Hole12, Hole13, Hole14, Hole15, Hole16, Hole17, Hole18)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (date, last_name, *scores))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)
