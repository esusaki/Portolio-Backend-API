from models import app, db, User, user_schema, posts_schema
from flask import request, jsonify

@app.route("/api/v1/user/<user_id>", methods = ["GET"])
def get_user(user_id):
    target_user = db.session.get(User, user_id)
    return jsonify(user_schema.dump(target_user))

@app.route("/api/v1/posts/<user_id>", methods = ["GET"])
def get_posts(user_id):
    target_user = db.session.get(User, user_id)
    target_posts = target_user.posts
    return jsonify(posts_schema.dump(target_posts))

@app.route("/api/v1/user", methods = ["POST"])
def create_user():
    new_user = User(
        # bio, Xはデフォルトではnull値になる
        user_id = request.json["user_id"],
        username = request.json["username"]
        )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(user_schema.dump(new_user))

if __name__ == "__main__":
    app.run(debug=True)