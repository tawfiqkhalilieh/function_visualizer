from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

@app.get('/polynomial/{a}/{b}/{c}')
def polynomial(a:float,b:float,c:float):
    from services.polynomial import fun
    return FileResponse(f"plots/{fun(a,b,c)}")

@app.get('/mxb/{m}/{b}')
def slope_intercept(m:float,c:float):
    from services.slope_intercept import fun
    return FileResponse(f"plots/{fun(m,c)}")