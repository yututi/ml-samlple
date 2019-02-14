# 機械学習サンプル

## 必要なもの
- Python3
- node.js

## クライアント側ビルド
```
cd {PROJECT_ROOT}/cl
npm install
npm run build
```

## サーバー起動
```
cd {PROJECT_ROOT}
python -m venv venv
.\venv\Scripts\activate # or /venv/Scripts/activate
(venv) pip install -r requirements.txt
(venv) cd sv
(venv) python manage.py runserver
```

## 2回目以降
```
cd {PROJECT_ROOT}
.\venv\Scripts\activate # or /venv/Scripts/activate
(venv) cd sv
(venv) python manage.py runserver
```
