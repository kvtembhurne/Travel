from flask import Flask, render_template

app = Flask(__name__)  # Corrected from _name_ to __name__

# Sample data for destinations
destinations = [
    {
        "name": "Heritage Site A",
        "details": "A historical site with rich cultural significance.",
        "routes": "Bus, Auto, Metro"
    },
    {
        "name": "Museum B",
        "details": "Learn about local history, artifacts, and art exhibitions.",
        "routes": "Metro, Auto"
    },
    {
        "name": "Park C",
        "details": "A serene park for relaxation and connecting with nature.",
        "routes": "Bus, Auto"
    },
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/explore")
def explore():
    return render_template("explore.html", destinations=destinations)

@app.route("/donate")
def donate():
    return render_template("donate.html")

if __name__ == "__main__":  # Corrected from _name_ to __name__
    app.run(debug=True)
