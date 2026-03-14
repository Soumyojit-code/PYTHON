from flask import Flask, render_template, request, redirect
from database import connect_db, create_table

app = Flask(__name__)

create_table()

@app.route("/")
def home():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    return render_template("index.html", expenses=expenses)


@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        category = request.form["category"]
        amount = request.form["amount"]
        description = request.form["description"]

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)",
            (category, amount, description)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_expense.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

