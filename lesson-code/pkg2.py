# this module records my personal information

name = 'Doris'
age = 19
location = 'germany'


def get_age():
    return age


def set_age(value):
    global age
    age = value
    return age