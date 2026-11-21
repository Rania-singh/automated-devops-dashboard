# Automated Build, Testing and Dashboard Deployment using DevOps

A beginner-friendly demonstration project combining a Python Flask health-check application, automated tests, Docker image building, GitHub Actions CI, and GitHub Pages deployment for a static pipeline dashboard.

## Components
- `app.py`: Flask application with `/` and `/health` endpoints.
- `tests/`: automated tests executed by pytest.
- `Dockerfile`: container image definition for the Flask application.
- `.github/workflows/ci-cd.yml`: tests the application, builds the Docker image, then deploys the dashboard in `site/` to GitHub Pages.
- `site/`: static dashboard explaining the pipeline.

## Run locally
```bash
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements-dev.txt
py -m pytest -q
py app.py
```
Open http://127.0.0.1:5000/ and http://127.0.0.1:5000/health.

## Build with Docker
```bash
docker build -t clouddevops-demo .
docker run --rm -p 5000:5000 clouddevops-demo
```

## GitHub Pages setup
1. Create a **public** GitHub repository and upload/push this project to the `main` branch.
2. In repository Settings → Pages → Build and deployment, select **GitHub Actions** as the source.
3. Open Actions and watch `CI and Dashboard Deployment`.
4. After a successful run, the dashboard URL appears in Settings → Pages and in the workflow deployment environment.

GitHub Pages is hosting the static dashboard. The Flask app is run locally or in Docker; this workflow does not deploy the Flask container to a cloud server. No AWS/GCP account is required. GitHub plan limits and current Pages eligibility apply.
