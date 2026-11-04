from flask_admin.contrib.sqla import ModelView

from eapp.models import Category, Product
from eapp import app, db
from flask_admin import Admin

admin = Admin(app=app, name='E-Commerce Admin')
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))