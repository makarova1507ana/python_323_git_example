# Создать БД с таблицей для класса Товар,
# добавить функционал по добалению,редактированию и удаления записей в талице, 
# Создать класс товар (имя, цена, тип)

import sqlite3 as sq

#
list_products = [('стул', 500 ,'мебель для зала '), ('стол', 1500 ,'мебель для зала '), ('диван', 20000 ,'мебель для зала ')]

# имитацию прохождения через файл product.py -> объект типа product


# ('стул', 500 ,'мебель для зала ') -> объект типа product


# объект типа product-> добавить в таблицу



# прототип функции 
def add_product():# добалениe Товарa
    pname, price, types = '0', 0, '0' 
    return f"INSERT INTO products (pname, price, types) VALUES ('{pname}', {price}, '{types}')"
  
   
with sq.connect("Shop.db") as con:
    cur = con.cursor()
 
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pname TEXT NOT NULL,
            price INTEGER DEFAULT 0,
            types TEXT NOT NULL); """)
    
# ----------------------Интерфейс по добалению,редактированию и удаления записей в талице------------------------------#
    # Функция добаления
    cur.executescript(add_product())
    
    result = cur.execute("SELECT * FROM products;")
    print(result.fetchall())

    # Функция редактирование товара
    
    # Функция удаления товара


