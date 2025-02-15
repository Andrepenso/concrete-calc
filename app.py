from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    custo_material = None
    concreto_usinado = None
    diferenca = None
    valores = {}

    if request.method == "POST":
        try:
            valores["areia"] = float(request.form["areia"])
            valores["agua"] = float(request.form["agua"])
            valores["cimento"] = float(request.form["cimento"])
            valores["brita"] = float(request.form["brita"])
            concreto_usinado = float(request.form["concreto_usinado"])

            custo_material = sum(valores.values())
            diferenca = concreto_usinado - custo_material

        except ValueError:
            return render_template("index.html", erro="Por favor, insira valores numéricos válidos.")

    return render_template("index.html", custo_material=custo_material, concreto_usinado=concreto_usinado, diferenca=diferenca, valores=valores)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
