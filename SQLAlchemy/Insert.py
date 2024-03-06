from Create_table import Staff, Clients, Products, Supplier, Supply, Orders, engine
from sqlalchemy.orm import Session

with Session(engine) as session:
    st1 = Staff(last_name='Иванов', name='Иван',
                middle_name='Иванович', status='Работник',
                address='Г.Москва, ул.Ленина, д. 45', home_phone=43210,
                birthday='19800101')
    st2 = Staff(last_name='Петров', name='Петр',
                middle_name='Петрович', status='Сотрудник',
                address='Г.Санкт - Петербург, ул.Нева, д.67', home_phone=61230,
                birthday='19780202')
    st3 = Staff(last_name='Сидоров', name='Сидор',
                middle_name='Сидорович', status='Менеджер',
                address='Г.Екатеринбург, ул.Шаумяна, д.121', home_phone=24412,
                birthday='19900608')
    st4 = Staff(last_name='Лебедев', name='Леонид',
                middle_name='Леонидович', status='Директор',
                address='Г.Новосибирск, ул.Проспект Ленина, д.1', home_phone=67890,
                birthday='19850303')
    st5 = Staff(last_name='Миронов', name='Мирон',
                middle_name='Миронович', status='Инженер',
                address='Г.Воронеж, ул.Советская, д.34', home_phone=4321,
                birthday='19920404')
    session.add_all([st1, st2, st3, st4, st5])
    cl1 = Clients(name="Залупенко Иван Степанович", address="Г. Екатеринбург, ул. Шаумяна, д. 121", phone=4412)
    cl2 = Clients(name="Прохоров Антон Георгиевич", address="Г. Екатеринбург, ул. Амунсена, д. 3", phone=4567)
    cl3 = Clients(name="Жиденко Василий Иванович", address="Г. Екатеринбург, ул. Шварца, д. 9", phone=91234)
    cl4 = Clients(name="Петропавловский Степан Денисович", address="Г. Екатеринбург, ул. Шаумяна, д.121",
                  phone=11111)
    cl5 = Clients(name="Швецко Анна Григорьевна", address="Г. Екатеринбург, ул. Кертонова, д. 10", phone=78901)
    session.add_all([cl1, cl2, cl3, cl4, cl5])
    sr1 = Supplier(name='ООО Радуга', name_delegate='Иванов Иван Иванович',
                   use_delegate='Ваня', phone=43210,
                   address='Г. Москва, ул. Ленина, д. 45')
    sr2 = Supplier(name='ООО Стройка', name_delegate='Петров Петр Петрович',
                   use_delegate='Петр', phone=1230,
                   address='Г. Санкт-Петербург, ул. Нева, д. 67')
    sr3 = Supplier(name='ООО Крутой поставщик', name_delegate='Француа Георг Шмидтович',
                   use_delegate='Крутой чел', phone=65457,
                   address='Г. Екатеринбург, ул. Ясная, д.1')
    sr4 = Supplier(name='ООО СтройМонтаж', name_delegate='Лебедев Леонид Леонидович',
                   use_delegate='Лебедь', phone=567890,
                   address='Г. Новосибирск, ул. Проспект Ленина, д. 1')
    sr5 = Supplier(name='ООО ТехноСервис', name_delegate='Миронов Мирон Миронович',
                   use_delegate='Мир', phone=54321,
                   address='Г. Воронеж, ул. Советская, д. 34')
    session.add_all([sr1, sr2, sr3, sr4, sr5])
    s1 = Supply(fk_supplier_id=sr2.supplier_id, date_delivery='20230101')
    s2 = Supply(fk_supplier_id=sr3.supplier_id, date_delivery='20230201')
    s3 = Supply(fk_supplier_id=sr1.supplier_id, date_delivery='20230301')
    s4 = Supply(fk_supplier_id=sr5.supplier_id, date_delivery='20230401')
    s5 = Supply(fk_supplier_id=sr4.supplier_id, date_delivery='20230501')
    session.add_all([s1, s2, s3, s4, s5])
    pr1 = Products(fk_supply_id=s2.supply_id,
                   name='Ноутбук Acer', specify='https://www.acer.com/ac/en/US/content/home',
                   description='Черный, 15 дюймов', image='https://www.acer.com/ac/en/US/content/home',
                   price_purchase=50000.00, available=True,
                   amount=50, price_sale=65000.00)
    pr2 = Products(fk_supply_id=s3.supply_id,
                   name='Смартфон Samsung', specify='https://www.samsung.com/ru/',
                   description='Белый, 6.5 дюймов', image='https://www.samsung.com/ru/',
                   price_purchase=25000.00, available=True,
                   amount=80, price_sale=32500.00)
    pr3 = Products(fk_supply_id=s1.supply_id,
                   name='Кроссовки Nike', specify='https://www.nike.com/',
                   description='Красный, размер 42', image='https://www.nike.com/',
                   price_purchase=5000.00, available=True,
                   amount=20, price_sale=6500.00)
    pr4 = Products(fk_supply_id=s4.supply_id,
                   name='Куртка The North Face', specify='https://www.thenorthface.com/',
                   description='Синий, размер L', image='https://www.thenorthface.com/',
                   price_purchase=10000.00, available=False,
                   amount=0, price_sale=13000.00)
    pr5 = Products(fk_supply_id=s2.supply_id,
                   name='Кофемашина DeLonghi', specify='https://www.delonghi.com/',
                   description='Серебристый, автоматическая', image='https://www.delonghi.com/',
                   price_purchase=20000.00, available=True,
                   amount=70, price_sale=26000.00)
    session.add_all([pr1, pr2, pr3, pr4, pr5])
    ord1 = Orders(fk_staff_id=st2.staff_id, fk_products_id=pr4.products_id, date_placement='20230201',
                  date_execution='20230204', fk_clients_id=cl5.clients_id)
    ord2 = Orders(fk_staff_id=st3.staff_id, fk_products_id=pr2.products_id, date_placement='20230401',
                  date_execution='20230410', fk_clients_id=cl1.clients_id)
    ord3 = Orders(fk_staff_id=st1.staff_id, fk_products_id=pr1.products_id, date_placement='20230701',
                  date_execution='20230712', fk_clients_id=cl3.clients_id)
    ord4 = Orders(fk_staff_id=st5.staff_id, fk_products_id=pr5.products_id, date_placement='20230901',
                  date_execution='20230906', fk_clients_id=cl2.clients_id)
    ord5 = Orders(fk_staff_id=st4.staff_id, fk_products_id=pr3.products_id, date_placement='20231001',
                  date_execution='20231011', fk_clients_id=cl4.clients_id)
    session.add_all([ord1, ord2, ord3, ord4, ord5])
    session.commit()
