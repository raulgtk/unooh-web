# coding: utf-8

import random

from lib.dbtools import db_add
from lib.dbtools import db_commit

def insert_sample_data():

    # users
    from .db_sample_data.users import user_list
    for user in user_list:
        db_add(user)
    db_commit()

    # countries
    from .db_sample_data.countries import country_list
    for country in country_list:
        db_add(country)
    db_commit()