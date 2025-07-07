FROM python:3.10
WORKDIR /app

# 1) Install dependencies
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 2) Copy the app code
COPY backend/app/ ./app/

# 3) Copy your prompts folder
COPY prompts/ ./prompts/

# 4) Expose and run
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
