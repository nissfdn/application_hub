from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Network_Subnet_Planner", methods=["GET", "POST"])
def app1():
    if request.method == "GET":
        return render_template("NetworkSubnetPlanner.html")
    if request.method == "POST":
        host_num = int(request.form["host_num"])  #html de int yazsak dahi flask her zaman str getiri html den bu yuzden int donusumu yapiyoruz
        print(host_num)


@app.route("/app2")
def app2():
    return render_template("app2.html")

@app.route("/app3")
def app3():
    return render_template("app3.html")

if __name__ == "__main__":
    app.run(debug=True)