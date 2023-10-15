from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/house_locations"  # Replace with your MongoDB URI
mongo = PyMongo(app)

@app.route("/")
def index():
    locations = mongo.db.locations.find()
    return render_template("index.html", locations=locations)

@app.route("/add_location", methods=["POST"])
def add_location():
    city = request.form.get("city")
    if city:
        mongo.db.locations.insert({"city": city})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
