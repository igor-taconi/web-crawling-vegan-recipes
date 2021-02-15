import sqlite3


class VeganRecipesPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connect = sqlite3.connect('recipes.db')
        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS recipe""")

        sql = """
            CREATE TABLE recipe(
                title TEXT,
                image TEXT,
                ingredients TEXT,
                preparation TEXT,
                time TEXT,
                url TEXT UNIQUE
            )
        """
        self.cursor.execute(sql)

    def db_insert(self, item):
        self.cursor.execute(
            """
            INSERT INTO recipe(
                title, image, ingredients, preparation, time, url
            )
                VALUES(
                '{}', '{}', '{}', '{}', '{}', '{}'
            )""".format(
                item['title'],
                item['image'],
                item['ingredients'],
                item['preparation'],
                item['time'],
                item['url'],
            )
        )
        self.connect.commit()

    def process_item(self, item, spider):
        self.db_insert(item)
        return item
