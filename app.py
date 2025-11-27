from flask import Flask, render_template, request
from physics import drop_at_distance, trajectory_no_drag
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for server
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

def plot_trajectory(v0, filename):
    # Always plot for angle = 0 (parallel to ground), starting 4 ft above ground
    points = trajectory_no_drag(v0, 0.0, step=1, initial_height=4.0)
    if not points or len(points) < 2:
        plt.figure(figsize=(8, 4))
        plt.text(0.5, 0.5, 'Trajectory too short to plot', ha='center', va='center')
        plt.axis('off')
        plt.savefig(filename)
        plt.close()
        return
    xs, ys = zip(*points)
    plt.figure(figsize=(8, 4))
    plt.plot(xs, ys, label="Trajectory (parallel to ground, 4 ft high)", color='blue', linewidth=2)
    plt.xlabel("Distance (ft)")
    plt.ylabel("Height (ft)")
    plt.title("Projectile Trajectory (ft)")
    plt.ylim(bottom=0)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None


    plot_url = None
    if request.method == "POST":
        try:
            v0 = float(request.form["v0"])

            static_dir = os.path.join(app.root_path, 'static')
            os.makedirs(static_dir, exist_ok=True)
            plot_path = os.path.join(static_dir, 'trajectory.png')
            plot_trajectory(v0, plot_path)
            plot_url = '/static/trajectory.png'

            result = {
                "v0": v0,
            }
        except (KeyError, ValueError):
            error = "Please enter valid numeric values."

    return render_template("form.html", result=result, error=error, plot_url=plot_url)

if __name__ == "__main__":
    app.run(debug=True)
