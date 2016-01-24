from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Shows the application form."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def application_confirmation():
    """Shows the application confirmation."""

    first_name = request.form.get("firstname")
    first_name = first_name.lower()
    first_name = first_name.capitalize()

    last_name = request.form.get("lastname")
    last_name = last_name.lower()
    last_name = last_name.capitalize()

    name = first_name + " " + last_name
    salary = request.form.get("salary")
    job = request.form.get("job")

    return render_template("application-response.html",
                           name=name,
                           salary=salary,
                           job=job)

if __name__ == "__main__":
    app.run(debug=True)
