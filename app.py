from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
   
    return render_template('index.html')
@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['search']

    conn = sqlite3.connect("food.db")
    cursor = conn.cursor()

    cursor.execute(
        """SELECT * FROM vendor WHERE name LIKE ?""",
        ('%' + keyword + '%',)
    )

    vendors = cursor.fetchall()
    conn.close()

    return render_template("view.html", vendors=vendors)
@app.route('/add')
def add():
    return render_template("add.html")
@app.route('/add', methods=['POST'])
def add_vendor():
    name = request.form['vendor_name']
    food = request.form['food_type']
    location = request.form['location']
    contact = request.form['contact']

    conn = sqlite3.connect('food.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO vendor(name, food, location, contact) VALUES (?,?,?,?)",
                   (name, food, location, contact))

    conn.commit()
    conn.close()

    return redirect('/')
@app.route('/view')
def view():
    conn = sqlite3.connect('food.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM vendor")
    data = cursor.fetchall()

    conn.close()

    return render_template("view.html", vendors=data)
@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('food.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM vendor WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect('/view')
@app.route('/edit/<int:id>')
def edit(id):
    conn = sqlite3.connect('food.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM vendor WHERE id=?", (id,))
    data = cursor.fetchone()
    conn.close()
    return render_template("edit.html",v=data)
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['vendor_name']
    food = request.form['food_type']
    location = request.form['location']
    contact = request.form['contact']

    conn = sqlite3.connect('food.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE vendor SET name=?, food=?, location=?, contact=? WHERE id=?",
                   (name, food, location, contact, id))

    conn.commit()
    conn.close()

    return redirect('/view')
    conn.close()

    return render_template("edit.html", v=data)
if __name__ == "__main__":

    app.run()
