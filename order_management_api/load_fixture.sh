#!/usr/bin/env bash

python order_management_api/manage.py loaddata order_management_api/fixture/roles.json
python order_management_api/manage.py loaddata order_management_api/fixture/products.json
python order_management_api/manage.py loaddata order_management_api/fixture/auth_user.json
python order_management_api/manage.py loaddata order_management_api/fixture/user.json

echo "OK"
