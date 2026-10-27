# Student Performance Demo — MLOps ISE-2 (Roll No. 08)

**Course:** ML DevOps Laboratory  
**Department:** CSE (Data Science)  
**Academic year:** 2026–27  
**Project:** Student Performance Prediction Web Application with CI/CD and Monitoring

## Problem statement

Build a small Flask web application and demonstrate the DevOps lifecycle using Git, GitHub, Jenkins, Docker, automated tests, and a health endpoint. The app accepts study hours and attendance and returns a simple rule-based demonstration category.

> **Important:** The current prediction is a transparent rule-based baseline, not a trained machine-learning model. Describe it accurately in the report. A trained model can be added as a future extension.

## Requirements

- Python 3.10+ (tested with Python 3.12 image in Docker)
- Git
- Docker Desktop (Windows)
- Jenkins with a Windows agent that has Python and Docker available

## Run locally on Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pytest -q
python app.py
```

Open `http://localhost:5000` in your browser. Check `http://localhost:5000/health` for `{"status":"ok"}`.

If PowerShell blocks virtual-environment activation, run `.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt` and `.\.venv\Scripts\python.exe -m pytest -q` instead.

## Run with Docker

```powershell
docker build -t student-performance-mlops .
docker run --rm -p 5000:5000 --name student-performance-mlops student-performance-mlops
```

Open `http://localhost:5000/health`. In another terminal, inspect the container:

```powershell
docker ps
docker logs student-performance-mlops
```

Stop it with `Ctrl+C` in the terminal running the container, or use `docker stop student-performance-mlops` from another terminal.

## Git and GitHub

Create an empty repository on GitHub named `student-performance-mlops-roll08`. Do not initialize it with a README because this project already has one. From this project folder:

```powershell
git init
git add .
git commit -m "Initial commit: Flask app with tests and Docker"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/student-performance-mlops-roll08.git
git push -u origin main
```

Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username. Never share your password or personal access token in a report or chat.

## Jenkins pipeline

The included `Jenkinsfile` checks out the repository, installs dependencies, runs pytest, and builds the Docker image. Create a Jenkins Pipeline job and select **Pipeline script from SCM**, SCM **Git**, and your repository URL; set the script path to `Jenkinsfile`.

The example uses Windows `bat` commands. The Jenkins agent must have Python, pip, Git, and Docker installed and available on PATH, and the Jenkins service account must be permitted to use Docker. If Jenkins runs on Linux, change `bat` steps to `sh` commands and use a suitable Linux agent.

## Monitoring / evidence

- Health endpoint: `GET /health` returns HTTP 200 with `{"status":"ok"}`.
- Docker status: `docker ps`
- Container logs: `docker logs student-performance-mlops`
- Automated tests: `python -m pytest -q`
- Capture genuine screenshots of the running app, health endpoint, GitHub repository, successful Jenkins build, and running Docker container for the report.

## Repository checklist

- [ ] Update student name in the report.
- [ ] Replace the example GitHub URL with your actual repository URL.
- [ ] Run the tests locally and record the actual output.
- [ ] Run the Docker image and verify `/health`.
- [ ] Configure and run Jenkins; capture the actual build result.
- [ ] Export the final report as PDF and submit it on ERP.

## Project structure

```text
student-performance-mlops-roll08/
├── app.py
├── test_app.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── Jenkinsfile
├── .dockerignore
├── .gitignore
└── README.md
```
