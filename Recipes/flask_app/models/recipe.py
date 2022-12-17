from flask_app.config.MySQLConnection import connect
from flask import flash
mydb = "recipes" #'' insted of ""

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.recipe_name = data['recipe_name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.min_30 = data['30_min']
        self.date_made = data['date_made']
        self.update_at = data['update_at']
        self.created_at = data['created_at']
        self.creator = None

    @classmethod
    def save(recipe,data): #change recipe to cls
        #print(data)
        query = '''
        INSERT INTO recipes 
        (recipe_name,description,instructions,min_30,date_made) 
        VALUES(%(recipe_name)s,%(description)s,%(instructions)s,%(min_30)s,%(date_made)s);'''
        results = connect(mydb).query_db(query, data)
        print(f"results: {results}")
        return results
    
    @classmethod
    def getById(cls, data):
        print(data)
        query = '''
        SELECT * 
        FROM recipes 
        WHERE id = %(id)s;'''
        results = connect(mydb).query_db(query, data)
        print(f"results: {results}")
        return cls(results[0])

    @classmethod
    def get_all_recipes(cls):
        query = '''
        SELECT *
        FROM recipes;'''
        results = connect(mydb).query_db(query)
        #pprint(results)
        output = []
        for row in results:
            output.append(cls(row))
            #print(output)
        return output

    @classmethod
    def deleteRecipeById(cls, data):
        print(data)
        query = '''
        DELETE FROM 
        recipes WHERE id = %(id)s;'''
        results = connect(mydb).query_db(query, data)
        print(f"results: {results}")