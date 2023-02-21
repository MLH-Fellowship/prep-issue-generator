# MLH Prep - Issue Generator    

This allows staff to create issues across all the individual pod repos by just pulling them directly from the template repository. Aim is to speed up setup time allowing us to scale.

*Make sure to add a GitHub Access Token to the `.env`. Use the one provided by the MLH Fellowship team.

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```
python3 app.py
```
