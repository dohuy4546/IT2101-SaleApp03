from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app import db, app

class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable = False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Product(db.Model):
    __tablename__= 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(255), default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg", nullable=True)
    active =Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100), default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')

if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        import hashlib
        u = User(name='Admin', username='admin', password=str(hashlib.md5('12345'.encode('utf-8')).hexdigest()))
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        # p1 = Product(name='iPhone 13', price=20000000, category_id=1)
        # p2 = Product(name='Galaxy S23 Plus', price=22000000, category_id=1)
        # p3 = Product(name='iPad Pro 2023', price=35000000, category_id=2)
        # p4 = Product(name='Galaxy Tab S9', price=24000000, category_id=2)
        # p5 = Product(name='Note 23', price=20000000, category_id=1)
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.commit()

