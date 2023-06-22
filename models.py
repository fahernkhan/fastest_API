from mysql.connector import connect
from dotenv import dotenv_values

params = dotenv_values(".env")

class Database:
    db = None
    def __init__(self):
        self.db = connect(
            username=params.get("MYSQL_USERNAME"),
            password=params.get("MYSQL_PASSWORD"),
            host=params.get("MYSQL_HOST"),
            port =params.get("MYSQL_PORT"),
            database =params.get("MYSQL_DB")
        )

    def search_movie_by_year(self, year):
        q = f'''
            SELECT
                movie_title as title,
                director_name as director,
                title_year as year
            FROM
                movies
            WHERE
                title_year = {year}
            ORDER BY
                movie_title
        '''

        cursor_db = self.db.cursor(dictionary=True)
        cursor_db.execute(q)
        result = cursor_db.fetchall()
        return [row for row in result]