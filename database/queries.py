class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS surveys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            half TEXT,
            type_pizza TEXT,
            purity TEXT
        )
    """
    DROP_TYPES_PIZZA_TABLE = "DROP TABLE IF EXISTS types_pizza"
    CREATE_TYPES_PIZZA_TABLE = """
        CREATE TABLE IF NOT EXISTS types_pizza (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """
    DROP_PIZZAS_TABLE = "DROP TABLE IF EXISTS pizzas"
    CREATE_PIZZAS_TABLE = """
        CREATE TABLE IF NOT EXISTS pizzas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            size  TEXT,
            price FLOAT,
            picture TEXT,
            type_pizza_id INTEGER,
            FOREIGN KEY(type_pizza_id) REFERENCES types_pizza(id)
        )
    """
    POPULATE_TYPES_PIZZA = """
        INSERT INTO type_pizza (name) VALUES
            ('С сыром'),
            ('Острые'),
            ('Без сыра')
    """
    POPULATE_PIZZAS = """
        INSERT INTO pizzas (name, size, price, picture, type_pizza_id) VALUES
        ('Пеперони', 'диаметр-30см', 300.0, 'images/pizza_1.jpg', 1),
        ('Маргарита', 'диаметр-35см', 300.0, 'images/pizza_2.jpg', 2),
        ('Сырная', 'диаметр-30см', 300.0, 'images/pizza_3.jpg', 3)
    """