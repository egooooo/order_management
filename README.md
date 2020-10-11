# ORDER MANAGEMENT

git clone ... \
cd order_management \
docker-compose up -d --build \
docker-compose run api python order_management_api/manage.py migrate \
docker-compose up 

# SWAGGER

http://localhost:8323/
