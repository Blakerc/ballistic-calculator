from flask import Flask, render_template, request
from physics import drop_at_distance

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            v0 = float(request.form["v0"])
            angle = float(request.form["angle"])
            distance = float(request.form["distance"])

            drop = drop_at_distance(v0, angle, distance)

            result = {
                "v0": v0,
                "angle": angle,
                "distance": distance,
                "drop": drop,
            }
        except (KeyError, ValueError):
            error = "Please enter valid numeric values."

    return render_template("form.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
