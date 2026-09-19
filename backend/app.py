from flask import Flask, request, jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reviews.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)



class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)

   
    rating = db.Column(db.Integer, nullable=False)

   
    review = db.Column(db.Text, nullable=False)

    
    best_pandal = db.Column(db.String(200), nullable=False)

    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)



@app.route("/review", methods=["GET", "POST"])
def review():

    
    if request.method == "GET":
        return render_template("review.html")

    
    if request.method == "POST":

        data = request.get_json()

       
        rating = data.get("rating")
        review_text = data.get("review")
        best_pandal = data.get("best_pandal")


        if not 1 <= int(rating) <= 5:
            return jsonify({
                "success": False,
                "message": "Rating must be between 1 and 5"
            }), 400

        new_review = Review(
          
            rating=int(rating),
            review=review_text,
            best_pandal=best_pandal
        )

        db.session.add(new_review)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Review submitted successfully!"
        })


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)