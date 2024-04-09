## 起動方法

### ①仮想環境を起動
venvフォルダと同じ階層で、以下のコマンドを入力
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
