# Smart Traffic Management System

## Overview
This system detects cars using AI, controls traffic signals, and provides congestion-based recommendations.

## Features
- AI-powered car detection (YOLO)
- Dynamic traffic signal optimization
- Web-based dashboard for visualization

## Installation
1. Install dependencies: `pip install -r requirements.txt`
2. Start the server: `python backend/app.py`
3. Open `http://127.0.0.1:5000` in a browser.

## Deployment
To deploy with Docker:
```bash
docker-compose up --build
