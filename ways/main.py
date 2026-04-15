from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()

weather_db = {
    'Mykolaiv': 'Sunny +17',
    'Kyiv': 'Cloudy +8',
    'TErnopil': 'Rainy +3'
}

@app.get('/weather/{city}')
#  http://127.0.0.1:8000/weather/Kyiv
def  get_weather(city: str):
    weather = weather_db.get(city)
    if weather:
        return {'city': city, 'weather': weather}
    raise HTTPException(status_code=404, detail='Місто не знайдено')


@app.get('/items/')
def list_items(skip: int = 0, limit = 10):
    return {'skip': skip, 'limit': limit}



@app.get('/info/')
async def get_info(accept: str = Header(default='application/json')):
    data = {'msg': 'це відповідь у форматі JSON'}

    if 'application/json' in accept:
        return JSONResponse(content=data)
    elif 'text/html' in accept:
        html_content = "<html><body><h1>This is an HTML response</h1></body></html>"
        return HTMLResponse(content=html_content)
    else:
        raise HTTPException(status_code=406, detail='Не приймається')