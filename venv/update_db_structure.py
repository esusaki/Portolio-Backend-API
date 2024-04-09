# 新しくテーブルの作成や、Columnの追加などを行いたい際は、以下の順序で行う

#   ①models.py に変更を加える
#   ②update_db_structure.py の実行 ←ここで実際にDBに変更が加わる

from models import app, db

with app.app_context():
    db.create_all()