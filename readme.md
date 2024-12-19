# GCP DevOps Project - Flask Application on GKE

## Overview
This project demonstrates the deployment of a Flask application within Docker containers, managed through Google Kubernetes Engine (GKE), with CI/CD implemented via Google Cloud Build.

## Architecture
The Flask application logs each request to the endpoint and returns a welcome message. It's containerized using Docker, automatically built, and deployed to GKE.

## Tools and Technologies
- **Flask**: Web framework for building the API.
- **Docker**: For containerizing the application.
- **Google Kubernetes Engine (GKE)**: For orchestrating the container deployment.
- **Google Cloud Build**: For CI/CD.
- **Google Container Registry (GCR)**: To store Docker images.

## Setup and Deployment Process
### Step 1: Dockerize the Flask App
Create a Dockerfile to containerize the application:
```Dockerfile
FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
```

### Step 2: Define the CI/CD Pipeline
- Use cloudbuild.yaml to define the Google Cloud Build configuration:
``` cloudbuild.yaml
steps:
  - name: 'docker'
    args:
      - 'build'
      - '-t'
      - 'gcr.io/$PROJECT_ID/gcpdevops'
      - '.'
  - name: 'gcr.io/cloud-builders/gke-deploy'
    args:
      - 'run'
      - '--filename=gke.yaml'
      - '--image=gcr.io/$PROJECT_ID/gcpdevops'
      - '--location=us-central1-c'
      - '--cluster=gcp-devops-project'
      - '--namespace=gcp-devops-prod'

images:
  - 'gcr.io/$PROJECT_ID/gcpdevops'

options:
  logging: CLOUD_LOGGING_ONLY

```
### Step 3: Kubernetes Deployment
- Use gke.yaml to deploy the Docker image to GKE:
  ```gke.yaml
  apiVersion: apps/v1
kind: Deployment
metadata:
  name: gcp-devops-gke
spec:
  replicas: 1
  selector:
    matchLabels:
      app: gcp
  template:
    metadata:
      labels:
        app: gcp
    spec:
      containers:
      - name: gcp-devops-gke
        image: gcr.io/$PROJECT_ID/gcpdevops:latest
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: gcp-devops-gke-service
  namespace: gcp-devops-prod
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: LoadBalancer

    ```
## Step 4: Access the Application

- After deployment, access the application through the external IP provided by the LoadBalancer.

![image](https://github.com/user-attachments/assets/c76680d2-7d4d-4c19-9680-8519f0a34a88)

![image](https://github.com/user-attachments/assets/3a668262-5e5f-4e66-8bca-678891f007e3)

