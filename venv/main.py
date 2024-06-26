# from models import app, db, User, user_schema, posts_schema, Post, URLSchema, URL, post_schema
from models import app, db, User, posts_schema, Post, post_schema, func_like_user_schema
from flask import request, jsonify
import os, time, datetime

os.environ["TZ"] = "Asia/Tokyo"

time.tzset()
time_now=datetime.datetime.now()

# GET
## 指定されたuser_idのユーザーの情報の取得
@app.route("/api/v1/user/<user_id>", methods = ["GET"])
def get_user(user_id):
    # if user_id in :
    #     target_user = db.session.get(User, user_id)
    #     # tartget_userがリスト
    #     return jsonify(func_like_user_schema(target_user)), 200
    # else:
    #     return jsonify({"error":"User not found"}), 404
    target_user = db.session.get(User, user_id)

    user_not_found = (target_user == None)

    if user_not_found:
        return jsonify({"message":"User Not Found. Check user_id."}), 404
    else:
        return jsonify(func_like_user_schema(target_user))

## 指定されたuser_idのユーザーの投稿一覧の取得
@app.route("/api/v1/posts/<user_id>", methods = ["GET"])
def get_posts(user_id):
    target_user = db.session.get(User, user_id)

    user_not_found = (target_user == None)

    if user_not_found:
        return jsonify({"message":"User Not Found. Check user_id."}), 404
    else:
        target_posts = target_user.posts
        return jsonify(posts_schema.dump(target_posts))

## 指定されたuser_idのpost_idの情報の取得
@app.route("/api/v1/post/<post_id>", methods = ["GET"])
def get_post_info(post_id):
    target_post = db.session.get(Post, post_id)

    post_not_found = (target_post == None)

    if post_not_found:
        return jsonify({"message":"Post Not Found. Check post_id."}), 404
    else:
        target_post_info = {
            "post_id" : post_id,
            "user_id" : target_post.user_id,
            "title" : target_post.title,
            "description" : target_post.description,
            "icon" : target_post.icon,
            "created_date" : target_post.created_date,
            "updated_date" : target_post.updated_date,
            "username" : target_post.user.username,
            "usericon" : target_post.user.photo_url
        }
        return jsonify(target_post_info)

#POST
## 新規ユーザーの作成
@app.route("/api/v1/user", methods = ["POST"])
def create_user():
    user_id_already_exists = (db.session.get(User, request.json["user_id"])!=None)

    if user_id_already_exists:
        return jsonify({"message":"user_id Already Exists."}), 403
    else:
        new_user = User(
            # bio, Xはデフォルトではnull値になる
            user_id = request.json["user_id"],
            username = request.json["username"],
            photo_url = request.json["photo_url"]
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(func_like_user_schema(new_user))

## 新規投稿の作成
@app.route("/api/v1/post/<user_id>", methods = ["POST"])
def create_post(user_id):
    target_user = db.session.get(User, user_id)

    user_not_found = (target_user == None)

    if user_not_found:
        return jsonify({"message":"User Not Found. Check user_id."}), 404
    else:
        new_post = Post(
            user_id = user_id,
            title = request.json["title"],
            description = request.json["description"],
            icon = request.json["icon"]
            #URLs = request.json["URL"]
        )
        db.session.add(new_post)
        db.session.commit()
        # for url in URLs:
        #     print(new_post.post_id)
        #     print("aiueo")
        #     new_url = URL(
        #         URL = url, 
        #         post_id = new_post.post_id
        #     )
        #     db.session.add(new_url)
        # db.session.commit()
        return jsonify(post_schema.dump(new_post))
        # return "aiueo"

# PUT
## 指定されたuser_idのユーザーの情報の更新
## とりあえず後から変える可能性があるのはbio, Xのみという設定
## usernameも変更するように変更
@app.route("/api/v1/user/<user_id>", methods = ["PUT"])
def update_user(user_id):
    target_user = db.session.get(User, user_id)

    user_not_found = (target_user == None)

    if user_not_found:
        return jsonify({"message":"User Not Found. Check user_id."}), 404
    else:
        target_user.username = request.json["username"]
        target_user.bio = request.json["bio"]
        target_user.X = request.json["X"]
        db.session.commit()
        return jsonify(func_like_user_schema(target_user))

## 指定されたpost_idの投稿の更新
@app.route("/api/v1/post/<post_id>", methods = ["PUT"])
def update_post(post_id):
    target_post = db.session.get(Post, post_id)

    post_not_found = (target_post == None)

    if post_not_found:
        return jsonify({"message":"Post Not Found. Check post_id."}), 404
    else:
        target_post.title = request.json["title"]
        target_post.description = request.json["description"]
        target_post.icon = request.json["icon"]
        db.session.commit()
        return jsonify(post_schema.dump(target_post))

# DELETE
## 指定されたpost_idの投稿の削除
@app.route("/api/v1/post/<post_id>", methods = ["DELETE"])
def delete_post(post_id):
    target_post = db.session.get(Post, post_id)

    post_not_found = (target_post == None)

    if post_not_found:
        return jsonify({"message":"Post Not Found. Check post_id."}), 404
    else:
        db.session.delete(target_post)
        db.session.commit()
        return jsonify(post_schema.dump(target_post))


if __name__ == "__main__":
    app.run(debug=True)