from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
#from flask_marshmallow import fields
from datetime import datetime
from flask_cors import CORS

from os.path import dirname, abspath, join

current_dir = dirname(abspath(__file__))

# SQLiteデータベースファイルの絶対パスを作成
db_file_path = join(current_dir, "var","models-instance", "database.db")

app = Flask(__name__)

CORS(app, resources={"*":{"origins":["http://localhost:3000", "https://portolio-zasetu.vercel.app"]}})

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_file_path

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    user_id = db.Column(db.String, primary_key = True)
    username = db.Column(db.String)
    bio = db.Column(db.String)
    X = db.Column(db.String)
    posts = db.relationship("Post", backref = "user")
    photo_url = db.Column(db.String)


# postsのリスト部分をうまく変換できないという問題が起きているため一旦user_schemaは使わない(func_like_user_schemaを使う)
#class UserSchema(ma.Schema):
#    class Meta:
#        fields = ("user_id","username","bio","X","posts")

#user_schema = UserSchema()
#users_schema = UserSchema(many = True)

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.String, db.ForeignKey("user.user_id"))
    title = db.Column(db.String)
    description = db.Column(db.String)
    icon = db.Column(db.String)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    # URLs = db.relationship("URL", backref="post")

class PostSchema(ma.Schema):
    class Meta:
        fields = ("post_id","user_id","title","description","icon","created_date","updated_date")
    #     fields = ("post_id","user_id","title","description","icon","created_date","updated_date","URLs")
    # URLs = fields.List() #上手く動かない

post_schema = PostSchema()
posts_schema = PostSchema(many = True)

def func_like_user_schema(_user_):
    ans = {}
    ans["user_id"] = _user_.user_id
    ans["username"] = _user_.username
    ans["bio"] = _user_.bio
    ans["X"] = _user_.X
    ans["photo_url"] = _user_.photo_url
    posts_by_user = []
    for post in _user_.posts:
        posts_by_user.append(post_schema.dump(post))
    ans["posts"] = posts_by_user
    return ans

# class URL(db.Model):
#     url_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
#     post_id = db.Column(db.Integer, db.ForeignKey("post.post_id"))
#     URL = db.Column(db.String)

# class URLSchema(ma.Schema):
#     class Meta:
#         fields = ("url_id","post_id","URL")

# url_schema = URLSchema()
# urls_schema = URLSchema(many = True)