# Fast API
https://fastapi.tiangolo.com/ja/

## コマンド
- uvicorn app.main:app --reload

## endpoint
- http://127.0.0.1:8000/
- 自動対話型の API ドキュメント[http://127.0.0.1:8000/docs]
- 代替の API ドキュメント[http://127.0.0.1:8000/redoc]

## チュートリアル
https://fastapi.tiangolo.com/tutorial/
- FastAPI は、API を定義するためのOpenAPI標準を使用して、すべての API を含む「スキーマ」を生成します。
- ファイル内のパスの順序は重要
    - 先に具体的なパスを設定する

## クエリパラメータ
https://fastapi.tiangolo.com/ja/tutorial/query-params/
- http://127.0.0.1:8000/items/?skip=0&limit=10
    - URLの一部なので文字列になる
    - async def read_item(skip: int = 0, limit: int = 10):の書き方だとその方に変換されてバリデーションが行われる。
        - ここで設定された値がデフォルト値になる
