from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)


app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "development-only-secret-key"
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reviews.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

CORS(app, origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://your-frontend.vercel.app"
])



class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    rating = db.Column(db.Integer, nullable=False)

    review = db.Column(db.Text, nullable=False)

    best_pandal = db.Column(db.String(200), nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


with app.app_context():
    db.create_all()


@app.route("/review", methods=["GET", "POST"])
def review():


    if request.method == "GET":
        return render_template("review.html")




    
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "success": False,
            "message": "Invalid request data"
        }), 400


    
    rating = data.get("rating")
    review_text = data.get("review")
    best_pandal = data.get("best_pandal")



    try:
        rating = int(rating)
    except (TypeError, ValueError):

        return jsonify({
            "success": False,
            "message": "Rating must be a number"
        }), 400


    if rating < 1 or rating > 5:

        return jsonify({
            "success": False,
            "message": "Rating must be between 1 and 5"
        }), 400




    if not isinstance(review_text, str):

        return jsonify({
            "success": False,
            "message": "Invalid review"
        }), 400


    review_text = review_text.strip()


    if not review_text:

        return jsonify({
            "success": False,
            "message": "Review cannot be empty"
        }), 400



    if len(review_text) > 1000:

        return jsonify({
            "success": False,
            "message": "Review must be 1000 characters or less"
        }), 400



    if not isinstance(best_pandal, str):

        return jsonify({
            "success": False,
            "message": "Invalid pandal name"
        }), 400


    best_pandal = best_pandal.strip()


    if not best_pandal:

        return jsonify({
            "success": False,
            "message": "Please select a pandal"
        }), 400


    if len(best_pandal) > 200:

        return jsonify({
            "success": False,
            "message": "Pandal name is too long"
        }), 400

    try:

        new_review = Review(
            rating=rating,
            review=review_text,
            best_pandal=best_pandal
        )

        db.session.add(new_review)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Review submitted successfully"
        }), 201


    except Exception:

        db.session.rollback()

        return jsonify({
            "success": False,
            "message": "Unable to save review"
        }), 500



if __name__ == "__main__":
    app.run(debug=False)

