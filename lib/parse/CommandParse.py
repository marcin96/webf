__author__ = 'Marcin'


def parse(text):
    data = text.split(" ")
    command=data[0]
    attributes=data[1:]
    return (command,attributes)