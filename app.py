from flask import Flask, render_template, redirect, request
# import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'flask_restaurant'
}

@app.route("/", methods=["GET"])
def home():
    # connection = mysql.connector.connect(**db_config)
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM add_menu")
    # menu_item = cursor.fetchall()
    # print(menu_item[1])

    # cursor.close()
    # connection.close()
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)