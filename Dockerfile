# Python image ni tanlaymiz
FROM python:3.12-slim

# Ishchi katalogni belgilaymiz
WORKDIR /app

# Talablar faylini nusxalaymiz
COPY requirements.txt /app/

# Talablarni o'rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# Loyiha fayllarini nusxalaymiz
COPY . /app/

# Django serverini ishga tushirish uchun buyruq
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
