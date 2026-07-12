from flask import Flask
app=Flask(__name__)
@app.get('/')
def index(): return 'Valentra Foundation'
if __name__=='__main__': app.run()
