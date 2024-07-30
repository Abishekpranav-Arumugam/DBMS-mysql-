from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as m
app = Flask(__name__)
d_obj = m.connect(host='localhost', database='database2', user='root', password='44-abcdef')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        roll_no = request.form['roll_no']
        mail = request.form['mail']
        phone_no = request.form['phone_no']
        cursor = d_obj.cursor()
        sql = "INSERT INTO stud (Name, Roll_no, Mail, Phone_no) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, roll_no, mail, phone_no))
        d_obj.commit()
        return redirect(url_for('index'))
    return render_template('insert.html')
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        new_name = request.form['new_name']
        cursor = d_obj.cursor()
        sql = "UPDATE stud SET Name=%s WHERE Roll_no=%s"
        cursor.execute(sql, (new_name, roll_no))
        d_obj.commit()
        return redirect(url_for('index'))
    return render_template('update.html')
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        cursor = d_obj.cursor()
        sql = "DELETE FROM stud WHERE Roll_no=%s"
        cursor.execute(sql, (roll_no,))
        d_obj.commit()
        return redirect(url_for('index'))
    return render_template('delete.html')
if __name__ == '__main__':
    app.run(debug=True)