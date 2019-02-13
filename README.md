# 機械学習サンプル

## クライアント側ビルド
```
cd cl
npm install
npm run build
```

## サーバー起動
```
python -m venv venv
.\venv\Scripts\activate # or /venv/Scripts/activate
(venv) python pip install -r requirements.txt
(venv) cd sv
(venv) python manage.py runserver
```

## 2回目以降
```
.\venv\Scripts\activate # or /venv/Scripts/activate
(venv) cd sv
(venv) python manage.py runserver
```
