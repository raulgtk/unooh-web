# coding=utf-8

from sqlalchemy import Column, String, Integer

from lib.dbtools import session
from lib.dbtools import Model

class Country(Model):
    __tablename__ = 'countries'

    code = Column(String, primary_key=True)
    name = Column(String)
    iso3 = Column(String)
    number = Column(Integer)

    @classmethod
    def get(cls, code=None):
        query = session.query(cls)
        if code:
            query = query.filter(cls.code == code)
        return query.one()

    @classmethod
    def query(cls, *args, **kwargs):
        return cls._query(*args, **kwargs).order_by(cls.name.asc()).all()

    @classmethod
    def _query(cls, codes=None, iso3s=None):
        query = session.query(cls)
        if codes:
            query = query.filter(cls.code.in_(codes))
        if iso3s:
            query = query.filter(cls.iso3.in_(iso3s))
        return query

    @classmethod
    def count(cls, *args, **kwargs):
        return cls._query(*args, **kwargs).count()

