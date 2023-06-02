from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"test": "This is the index , please check the docs for more info"}

 #input is a string
 #output is only builtin python data type

@app.get("/sum")
def sum(a,b):
    result=int(a)+int(b)
    return {'result':result}

@app.get("/multiply")
def multiply(a,b):
    result=int(a)*int(b)
    return {'result':result}

if __name__ == "__main__":
    print(read_root())
