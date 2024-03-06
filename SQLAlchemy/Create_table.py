from sqlalchemy import create_engine, ForeignKey
from datetime import date
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
engine = create_engine('postgresql://postgres:1234@localhost/itmentorsqla', echo=True)


class Base(DeclarativeBase):
    pass


class Staff(Base):
    __tablename__ = 'staff'

    staff_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    last_name: Mapped[str]
    name: Mapped[str]
    middle_name: Mapped[str]
    status: Mapped[str]
    address: Mapped[str]
    home_phone: Mapped[int]
    birthday: Mapped[date]
    addresses_st_ord: Mapped[list['Orders']] = relationship(back_populates='addresses_ord_st')


class Clients(Base):
    __tablename__ = 'clients'

    clients_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    address: Mapped[str]
    phone: Mapped[int]
    addresses_cl_ord: Mapped[list['Orders']] = relationship(back_populates='addresses_ord_cl')


class Products(Base):
    __tablename__ = 'products'

    products_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fk_supply_id: Mapped[int] = mapped_column(ForeignKey('supply.supply_id'))
    name: Mapped[str]
    specify: Mapped[str]
    description: Mapped[str]
    image: Mapped[str]
    price_purchase: Mapped[float]
    available: Mapped[bool]
    amount: Mapped[int]
    price_sale: Mapped[float]
    addresses_pr_s: Mapped['Supply'] = relationship(back_populates='addresses_s_pr')
    addresses_pr_ord: Mapped[list['Orders']] = relationship(back_populates='addresses_ord_pr')


class Supplier(Base):
    __tablename__ = 'supplier'

    supplier_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    name_delegate: Mapped[str]
    use_delegate: Mapped[str]
    phone: Mapped[int]
    address: Mapped[str]
    addresses_sr_s: Mapped[list['Supply']] = relationship(back_populates='addresses_s_sr')


class Supply(Base):
    __tablename__ = 'supply'

    supply_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fk_supplier_id: Mapped[int] = mapped_column(ForeignKey('supplier.supplier_id'))
    date_delivery: Mapped[date]
    addresses_s_sr: Mapped['Supplier'] = relationship(back_populates='addresses_sr_s')
    addresses_s_pr: Mapped[list['Products']] = relationship(back_populates='addresses_pr_s')


class Orders(Base):
    __tablename__ = 'orders'

    orders_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fk_staff_id: Mapped[int] = mapped_column(ForeignKey('staff.staff_id'))
    fk_products_id: Mapped[int] = mapped_column(ForeignKey('products.products_id'))
    date_placement: Mapped[date]
    date_execution: Mapped[date]
    fk_clients_id: Mapped[int] = mapped_column(ForeignKey('clients.clients_id'), nullable=False)
    addresses_ord_st: Mapped['Staff'] = relationship(back_populates='addresses_st_ord')
    addresses_ord_pr: Mapped['Products'] = relationship(back_populates='addresses_pr_ord')
    addresses_ord_cl: Mapped['Clients'] = relationship(back_populates='addresses_cl_ord')


Base.metadata.create_all(engine)
