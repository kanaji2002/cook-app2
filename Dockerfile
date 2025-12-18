# Python 3.13
FROM python:3.13-slim

# Python の余計なファイルを作らない
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 作業ディレクトリ
WORKDIR /app

# 依存関係を先にコピー（キャッシュ効率UP）
COPY requirements.txt /app/

# pip install
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクト全体をコピー
COPY . /app/


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
