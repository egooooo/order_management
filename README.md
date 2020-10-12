# ORDER MANAGEMENT

git clone https://github.com/egooooo/order_management.git \
cd order_management \
docker-compose up -d --build \
docker-compose run api python order_management_api/manage.py migrate \
docker-compose run api sh order_management_api/load_fixture.sh \
docker-compose up 

# SWAGGER

http://localhost:8323/
