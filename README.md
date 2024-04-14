# Portolioについて

Portolioは、サポーターズ主催の技育ハッカソン（2024年4月）にて、即席チーム（5人）で作成したサイトです。優秀賞を受賞しました。

バックエンドは、[@kuro](https://github.com/sp1st) と [@esusaki](https://github.com/esusaki) の2名で担当しました。

こちらの [作品URL](https://portolio-zasetu.vercel.app/) から、実際に使うことができます。

# 技術

バックエンド側では、FlaskとSQLAlchemyを使用し、データベースとのやり取りを行うAPIを作成しました。

APIのデプロイには、PythonAnywhereを使用しました。

フロントの技術や、作品全体の説明については、[フロントのリポジトリ](https://github.com/balckowl/portolio) もあわせてご覧ください。


# ローカルでのAPIの起動方法

### ①仮想環境をアクティブにする
venvフォルダと同じ階層で、以下のコマンドを入力

(※Mac以外の場合はコマンドが違うかも...すみません🙇)
```bash
source venv/bin/activate
```

### ②main.pyの実行
main.pyと同じ階層に移動後、以下のコマンドを入力

```bash
python main.py
or
python3 main.py
```

### ③ブラウザで http://127.0.0.1:5000/api/v1/user/aiueo123 にアクセス

以下のような感じでユーザーの情報が表示されたらOK


{
  "X": null,
  "bio": null,
  "posts": [],
  "user_id": "aiueo123",
  "username": "yamada"
}
