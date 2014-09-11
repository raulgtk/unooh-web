# coding: utf-8

from lib.geo import Country
from lib.geo.fixtures.countries import countries

country_list = []

for k,v in countries.items():
    country_list.append(
        Country(code=k, iso3=v['iso3'], number=v['number'], name=v['name']))
