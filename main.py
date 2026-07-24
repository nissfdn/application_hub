from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to the Flask App</h1>
    <ul>
        <li><a href="/app1">App 1 - Multiplication</a></li>
        <li><a href="/app2">App 2</a></li>
        <li><a href="/app3">App 3</a></li>
    </ul>
    """

@app.route("/app1", methods=["GET", "POST"])
def app1():
    result = None

    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        result = num1 * num2

    return f"""
    <h2>Multiplication Calculator</h2>

    <form method="POST">
        Number 1:
        <input type="number" step="any" name="num1" required><br><br>

        Number 2:
        <input type="number" step="any" name="num2" required><br><br>

        <input type="submit" value="Multiply">
    </form>

    <br>
    <h3>Result: {result if result is not None else ""}</h3>

    <a href="/">Back to Home</a>
    """

@app.route("/app2")
def app2():
    return "<h2>This is App 2</h2>"

@app.route("/app3")
def app3():
    return "<h2>This is App 3</h2>"

if __name__ == "__main__":
    app.run(debug=True)