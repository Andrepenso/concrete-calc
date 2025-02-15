from flask import Flask, render_template, request

app = Flask(__name__)  # Certifique-se de que esta linha está presente!

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            areia = float(request.form["areia"])
            agua = float(request.form["agua"])
            cimento = float(request.form["cimento"])
            brita = float(request.form["brita"])
            concreto_usinado = float(request.form["concreto_usinado"])

            custo_material = areia + agua + cimento + brita
            diferenca = concreto_usinado - custo_material

            return render_template("index.html", custo_material=custo_material, concreto_usinado=concreto_usinado, diferenca=diferenca)
        except ValueError:
            return render_template("index.html", erro="Por favor, insira valores numéricos válidos.")

    return render_template("index.html", custo_material=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
