from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # Inicializa os valores padrão
    valores = {
        "areia": 0.0, "agua": 0.0, "cimento": 0.0, 
        "brita": 0.0, "aditivo": 0.0, "concreto_usinado": 0.0
    }
    custo_material = None
    diferenca = None
    mais_caro = None
    erro = None

    if request.method == "POST":
        try:
            # Obtém os valores do formulário e converte para float
            valores["areia"] = float(request.form["areia"])
            valores["agua"] = float(request.form["agua"])
            valores["cimento"] = float(request.form["cimento"])
            valores["brita"] = float(request.form["brita"])
            valores["aditivo"] = float(request.form["aditivo"])
            valores["concreto_usinado"] = float(request.form["concreto_usinado"])

            # Traço padrão para 1m³ de concreto (1:2:3)
            tracado = {
                "cimento": 7,  # sacos por m³
                "areia": 0.6,  # m³
                "brita": 0.8,  # m³
                "agua": 180,   # litros
                "aditivo": 2   # litros
            }

            # Calcula o custo total dos materiais para 1m³ de concreto
            custo_material = (
                (tracado["cimento"] * valores["cimento"]) +
                (tracado["areia"] * valores["areia"]) +
                (tracado["brita"] * valores["brita"]) +
                (tracado["agua"] * valores["agua"]) +
                (tracado["aditivo"] * valores["aditivo"])
            )

            # Calcula a diferença entre concreto usinado e feito na obra
            diferenca = valores["concreto_usinado"] - custo_material
            mais_caro = diferenca > 0  # Verdadeiro se o usinado for mais caro
            diferenca = abs(diferenca)  # Calcula o valor absoluto no Python

        except ValueError:
            erro = "Por favor, insira valores numéricos válidos."

    return render_template("index.html", valores=valores, custo_material=custo_material, diferenca=diferenca, mais_caro=mais_caro, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)
