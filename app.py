from flask import Flask, render_template, request, redirect
from database import init_db, add_employee, get_employees

app = Flask(__name__)

init_db()

@app.route("/", methods=["GET"])
def index():
    employees = get_employees()
    return render_template("index.html", employees=employees)

@app.route("/employees", methods=["POST"])
def add():
    name = request.form.get("employee")
    if name:
        add_employee(name)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)