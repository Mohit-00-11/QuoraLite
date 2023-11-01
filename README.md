# QuoraXerox
Craft a Quora-Inspired Website for Inquisitive Minds.

## Prerequisites

1. Python 3.8 or higher.
2. Git (for cloning the repository).

## Getting Started

Follow these steps to set up and run the project on your local machine.

### 1. Clone project on working dir

```bash

git clone https://github.com/Mohit-00-11/QuoraXerox.git

```
### 2. Create a Virtual Environment

```bash
# On macOS and Linux
python3 -m venv venv

# On Windows
python -m venv venv

```
### 3. Activate the Virtual Environment

```bash

source venv/bin/activate

```

### 4. Install Requirements

```bash
pip install -r requirements.txt

```

### 5. Apply Migrations

```bash

python manage.py migrate

```
### 6. Run the Project

```bash
python manage.py runserver

```