from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    custo_material = None
    concreto_usinado = None
    diferenca = None
    valores = {"areia": "", "agua": "", "cimento": "", "brita": "", "concreto_usinado": ""}

    if request.method == "POST":
        try:
            valores["areia"] = request.form["areia"]
            valores["agua"] = request.form["agua"]
            valores["cimento"] = request.form["cimento"]
            valores["brita"] = request.form["brita"]
            valores["concreto_usinado"] = request.form["concreto_usinado"]

            custo_material = sum(float(valores[k]) for k in valores if k != "concreto_usinado")
            concreto_usinado = float(valores["concreto_usinado"])
            diferenca = concreto_usinado - custo_material

        except ValueError:
            return render_template("index.html", erro="Por favor, insira valores numéricos válidos.", valores=valores)

    return render_template("index.html", custo_material=custo_material, concreto_usinado=concreto_usinado, diferenca=diferenca, valores=valores)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
