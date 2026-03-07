
FROM python:3.10-slim

WORKDIR /app

# Instalējam atkarības reproducējami (vienādi katru reizi)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopējam tikai to, kas vajadzīgs lietotnes darbībai
COPY app.py .

CMD ["python", "app.py"]