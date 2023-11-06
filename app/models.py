from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app

class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable = False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    __tablename__= 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(255), default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg", nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        pass
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.commit()
        # p1 = Product(name='iPhone 13', price=20000000, category_id=1)
        # p2 = Product(name='Galaxy S23 Plus', price=22000000, category_id=1)
        # p3 = Product(name='iPad Pro 2023', price=35000000, category_id=2)
        # p4 = Product(name='Galaxy Tab S9', price=24000000, category_id=2)
        # p5 = Product(name='Note 23', price=20000000, category_id=1)
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.commit()

