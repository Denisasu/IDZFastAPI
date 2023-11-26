from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"FIO": "Лопушанский Денис Константинович"}

@app.get('/users')
async def f_indexU():
    return {"Contacts": "+79635786076"}

@app.get('/tools')
async def f_indexT():
    return {"About me": "Я обладаею опытом и навыками в области разработки сайтов, владею некоторыми языками программирования и так же изучаю, учусь работать с базами данных."}

