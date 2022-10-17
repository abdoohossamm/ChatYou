# ChatYou
ChatYou is an open source chat application.
### Prerequisites:
- GIT (latest)
- Python ≥ 3.8
- Docker Desktop or (Docker Engine and Docker Compose) if run using docker
- Any code editor or IDE (PyCharm recommended for Python and Django)
- Any database client (optional)
- Redis (if run locally)
## Installation

Clone the project

```bash
git clone https://github.com/abdoohossamm/ChatYou.git
```

Change directory to the cloned project

```bash
cd ChatYou
```

Make a copy of the example environment variables file and call it `.env`

```bash
cp .env.example .env
```

## Run the project
There are two ways to use docker compose depends on the docker version:

* Docker:
```bash
docker compose up
```
* Locally:

create a virtual environment
```bash
cd backend
python -m venv venv
```
##### activating the virtual environment depends on the OS please serach for it

Install requirements packages after activating the virtual environment
```bash
pip install -r requirements.txt
```
migrate the model
```bash
python manage.py migrate
```

create a user to test with
```bash
python manage.py createsuperuser
```

run django server
```bash
python manage.py runserver
```

## Add new chat room:
- go to this url: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- enter the admin user
- go to chat section click on room and click add room
- then you can go to this url: [http://127.0.0.1:8000/chat/](http://127.0.0.1:8000/chat/)
- now you can use the room to chat with friends