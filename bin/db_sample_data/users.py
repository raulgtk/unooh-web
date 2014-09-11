# coding: utf-8

from lib.user import User

user_list = []

## admin
admin = User()
admin.name = u"Admin User"
admin.email = "admin@domain.com"
admin.set_password('admin1234')
admin.role = "admin"
user_list.append(admin)