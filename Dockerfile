FROM python:3.8-slim-buster

WORKDIR /app

# Copying and installing the requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copying the rest of the application
COPY . .

# Command to run the application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
