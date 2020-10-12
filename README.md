# ORDER MANAGEMENT
It is a system for managing orders in a hardware store.

## Installation
Clone the project to a convenient directory
```bash
git clone https://github.com/egooooo/order_management.git
```
Go to the directory with the project
```bash
cd order_management
```
Start creating containers
```bash
docker-compose up -d --build 
```
Installing migrations
```bash
docker-compose run api python order_management_api/manage.py migrate
```
Installing fixtures
```bash
docker-compose run api sh order_management_api/load_fixture.sh
```
Launch of the project
```bash
docker-compose up 
```

## SWAGGER
After starting the project, we can go - [SWAGGER URL](http://localhost:8323/)
