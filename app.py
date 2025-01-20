from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

#connecting the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    # rows will convert to dictionaries
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    bowls = conn.execute('SELECT * FROM bowls').fetchall()
    conn.close()
    return render_template('index.html', bowls=bowls)

# Add a new bowl
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        conn = get_db_connection()
        conn.execute('INSERT INTO bowls (name, description) VALUES (?, ?)', (name, description))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('edit.html', item=None)

# Edit an existing item
@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    bowl = conn.execute('SELECT * FROM bowls WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        conn.execute('UPDATE bowls SET name = ?, description = ? WHERE id = ?', (name, description, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit.html', bowl=bowl)

# Delete an item
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM bowls WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
