# Assignment4
vendor managment system

# Installation Process
1. create vurtual env
2. activate env
3. Install requirments.txt "pip install -r requirments.txt
4. I attached my default database with data in project
                    or
5. Other wise setup your database
   "DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydatabase",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}"
6. create migrations file "python manage.py makemigrations"
7. create table in database "python namage.pymigrate"
8. Then run the project "python manage.py runserver"


# Example Data and EndPoint of api
1.create vendor and show all vendor list 
endpoint :- http://127.0.0.1:8000/api/vendors/
data:-{
        "name": "test2vendor",
        "contact_details": "demo details",
        "address": "kolkata 700001",
        "vendor_code": "demo1234546"
    }
2.edit/view/delete the vendor

endpoint:- http://127.0.0.1:8000/api/vendors/{vendor_id}

edit_data:-{
        "name": "test2vendor",
        "contact_details": "demo details",
        "address": "kolkata 700001",
        "vendor_code": "demo1234546"
    }

3.create/ view order

endpoint:- http://127.0.0.1:8000/api/purchase_orders/

post_data : - {
        "po_number": "6565657",
        "order_date": "2023-12-10T10:07:04Z",
        "delivery_date": "2023-12-11T10:07:13Z",
        "items": {
            "id": "000145",
            "type": "donghgut",
            "name": "Cakgdfge",
            "ppu": 0.55
        },
        "quantity": 4,
        "issue_date": "2023-12-10T10:08:36Z",
        "vendor": 1
    }

4.edit/view/delete order

endpoint:- http://127.0.0.1:8000/api/purchase_orders/{po_id}  #example=2

edit_data : - {
        "po_number": "6565657",
        "order_date": "2023-12-10T10:07:04Z",
        "delivery_date": "2023-12-11T10:07:13Z",
        "items": {
            "id": "000145",
            "type": "donghgut",
            "name": "Cakgdfge",
            "ppu": 0.55
        },
        "quantity": 6,
        "issue_date": "2023-12-10T10:08:36Z",
        "vendor": 1
    }

5. after complete the order user/cusomer give rating(extra api)

endpoint:-http://127.0.0.1:8000/api/order_complete/{po_id}

post_data = {
          "quality_rating":4
           }

6. vendor performance(get api)

endpoint:- http://127.0.0.1:8000/api/vendors/1/performance/

7. vendor_filter api

endpoint:-http://127.0.0.1:8000/vendors/?name=test

Note **you can search by any fields