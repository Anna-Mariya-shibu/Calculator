from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operator = request.form["operator"]

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"
            else:
                result = "Invalid operator"
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template("hello.html", result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
