# coding: utf-8

from sqlalchemy.engine import reflection
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData, Table, DropTable, ForeignKeyConstraint, DropConstraint

from .models.db import engine  # noqa
from .models.db import session  # noqa
from .models.db import Model  # noqa

def db_add(instance):
    session.add(instance)

def db_flush():
    session.flush()

def db_commit():
    session.commit()

def db_rollback():
    session.rollback()

def db_delete(instance):
    session.delete(instance)

def create_all():
    Model.metadata.create_all(bind=engine)

def drop_all(uri, echo=False):
    """ Delete all tables from database """
    
    engine = create_engine(uri, echo=echo)
    conn = engine.connect()
    trans = conn.begin()
    inspector = reflection.Inspector.from_engine(engine)
    metadata = MetaData()

    tbs = []
    all_fks = []

    for table_name in inspector.get_table_names():
        fks = []
        for fk in inspector.get_foreign_keys(table_name):
            if not fk['name']:
                continue
            fks.append(ForeignKeyConstraint((), (), name=fk['name']))
        t = Table(table_name, metadata, *fks)
        tbs.append(t)
        all_fks.extend(fks)

    for fkc in all_fks:
        conn.execute(DropConstraint(fkc))

    for table in tbs:
        conn.execute(DropTable(table))

    trans.commit()

