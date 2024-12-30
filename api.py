# Copyright (c) 2024 Vikas-06978
# Licensed under the MIT License
# Unauthorized copying of this file, via any medium, is strictly prohibited
# Written by Vikas

from flask_restful import Resource, Api
from app import app 
from models import Category

api = Api(app)

class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        return {'categories': [{
            'id' : category.id, 
            'name' : category.name
        }   for category in categories]
        }

api.add_resource(CategoryResource, '/api/category')
