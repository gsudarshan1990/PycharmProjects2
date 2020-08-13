#What is user defined exception?

class newexception(Exception):
    pass

def new_exception():
    raise newexception

new_exception()