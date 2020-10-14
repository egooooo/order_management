# ORDER MANAGEMENT
It is a simple order management system in a hardware store.

* Project was tested on manOS Catalina Version 10.15.7 and ubuntu 20.04 

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
Next step - run **SWAGGER**

## SWAGGER
**After starting the project, we can go** - [SWAGGER URL](http://localhost:8323/) or http://localhost:8323/


## Users:
1. Admin. \
	login: ``admin@admin.com`` \
	password: ``123qwe321``

Роль Администратора нужна для просмотра существующих ролей. 
Так же администратор может создать кассира, продовца-консультанта, бухгалтера.

2. Cashier. \
	login: ``cashier@cashier.com`` \
	password: ``123qwe321``

Роль кассира нужна для создания заказа и подтверждения оплаты заказа.

3. Shop Assistant. \
	login: ``shop_assistant@sa.com`` \
	password: ``123qwe321``

Роль продавец-консультант нужна для подтверждения нового сформированного заказа. 
То есть, консультант смотрит на заказ, проверяет чтобы все было правильно и в случае успеха, 
меняет статус что позволяет кассиру принять оплату клиента и выдать товар.

3. Accountant. \
	login: ``accountant@accountant.com`` \
	password: ``123qwe321``

Роль бухгалтера нужна для контроля средств. Может видеть все заказы в данный момент, с любым статусом. 

## USE CASE
1. **Авторизация**: \
Авторизоваться в сваггере в трех окнах. 
- В первом окне заходим под юзером кассир.
- Второе окно под юзером продавец-консультант. 
- Третье окно с ролью бухгалтер

Для этого необходимо перейти в раздел ``Auth`` метод ```POST /auth/login/``` и 
ввести данные юзера, все данные предоставлены выше. \
После авторизации под каким-то из юзеров можно посмотреть данные про роль, токен и тд. 
Копируем полученый токен и вставляем в поле ``Authorize``.

2. **Создать заказ**: \
Посмотреть список товаров можно в разделе ``Product`` методом ``GET ../product/``. 
Чтобы создать заказ, находим необходимый ``id`` товара и переходим в раздел Order. 
Вставляем ``id`` товара в ``POST ../product/order/`` под ролью кассир 
(если создать заказ под другой ролью увидим сообщение про ошибку). 
Заказ создан. В разделе ``Order``, метод ``GET ../product/order/`` кассир может 
посмотреть только те заказы, которые подтвердил продавец-консультант. 
* Проверка на скидку заложена в момент создания заказа. 
Один из лучших вариантов это поставить селери, который каждую ночь к примеру в 
12:00 будет проверять весь список товаров на срок, больше месяца или же нет и 
если больше, давать скидку.

4. **Оплата заказа**: \
Все суммы указаны в копейках. Переходим в раздел ``Order`` метод ``PUT ../product/order/{order_id}/.`` 
В поле ``order_id`` вставляем ``id`` заказа, в поле ``amount`` - сумма к оплате. 
Если в поле ``is_cash`` значение ``True``, то оплата наличными, если ``False`` - 
оплата картой(в таком случае поле amount можно не заполнять). Поле ``shop_assistant_check_product`` 
не нужно заполнять.

4. **Оплата заказа**: \
Все суммы указаны в копейках. Переходим в раздел ``Order`` метод ``PUT ../product/order/{order_id}/``. 
В поле ``order_id`` вставляем ``id`` заказа, в поле ``amount`` - сумма к оплате. 
Если в поле ``is_cash`` значение ``True``, то оплата наличными, если 
``False`` - оплата картой(в таком случае поле amount можно не заполнять). 
Поле ``shop_assistant_check_product`` не нужно заполнять. Отправляем запрос
(в этот момент заказ меняет свой статус на Оплачен и создается запись в таблице транзакций(Payments)) 
и получаем чек. В чеке есть информация о названии товара, стоимости товара, 
сумма, которую оплатил клиент, дата создания заказа, дата создания счёта, 
имя кассира, скидка, сдача, способ оплаты (наличные, карта).

## DELETE CONTAINERS
And at the end, you can use the command to clean the project container. 
