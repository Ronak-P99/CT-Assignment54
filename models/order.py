from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Order(Base):
    __tablename__ = 'Orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    total_price:Mapped[float] = mapped_column(nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('Customers.id'))
    product_id: Mapped[int] = mapped_column(db.ForeignKey('Products.id'))

    customer: Mapped["Customer"] = db.relationship(back_populates="Orders")
    product: Mapped["Product"] = db.relationship(back_populates="Orders")