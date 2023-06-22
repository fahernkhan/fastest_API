from models import Database

def search_movie_by_year(year):
    search_result = Database().search_movie_by_directors_name(year)
    return search_result