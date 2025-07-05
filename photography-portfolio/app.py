from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    cursor.execute("SELECT * FROM photos ORDER BY uploaded_at DESC")
    photos = cursor.fetchall()
    return render_template('gallery.html', photos=photos)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return redirect('/')
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
