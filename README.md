# Resume API (Local DevOps Project)

## What is this?

A simple API that returns a resume message.  
Built with Flask, Dockerized, and deployed with GitHub Actions CI/CD.

## How to Run Locally

```bash
docker build -t resume-api .
docker run -p 5000:5000 resume-api
```