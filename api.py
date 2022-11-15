from fastapi import FastAPI, Request
from datetime import datetime


storage = FastAPI(title = 'my FASTAPI')
#flash way
@storage.get('/')#ROUTE
def index():
    return "My name is Gloria, This is my API"


@storage.get('/today')
def today():
    return str(datetime.now())

    
@storage.get('/mynames')
def names(First_name: bool = False, last_name: bool = False, full_name: bool = True):
    full_names = ""
    if First_name:
        full_names += 'Gloria'
    if last_name:
        full_names += 'Sinseswa'
    if full_name:
        full_names = 'Hello my name is Gloria Sinseswa'
    return full_names






# from fastapi import FastAPI




# storage=FastAPI(title='Fast api')

# @storage.get('/')
# def index():
#     return 'this is my fastapi server  and let go to it !!!'
  

  
    

# if __name__ == '__main__':
#    app.run()

