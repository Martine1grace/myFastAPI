from fastapi import FastAPI




app=FastAPI(title='Fast api')

@app.get('/')
def index():
    return 'this is my fastapi server page'
  

  
    

if __name__ == '__main__':
   app.run()

