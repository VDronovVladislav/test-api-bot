FROM python:3.12.1

WORKDIR /bot

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["python", "main.py"]