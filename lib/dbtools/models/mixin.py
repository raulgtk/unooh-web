# coding: utf-8

from sqlalchemy import Column, Integer

from .db import session  # noqa

class ModelMixin(object):

    id = Column(Integer, primary_key=True)

    @classmethod
    def get(cls, id=None):
        query = session.query(cls)
        if id:
            query = query.filter(cls.id == id)
        return query.one()

    @classmethod
    def query(cls, *args, **kwargs):
        return cls._query(*args, **kwargs).all()

    @classmethod
    def count(cls, *args, **kwargs):
        return cls._query(*args, **kwargs).count()

    @classmethod
    def _query(cls, ids=None):
        query = session.query(cls)
        if ids:
            query = query.filter(cls.id.in_(ids))
        return query

