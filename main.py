from aiohttp import web
import requests
import isbnlib


routes = web.RouteTableDef()


async def DBconn():
    conn = psycopg2.connect("dbname='neprav-db' user='univ' host='127.0.0.1' port='5432' password='12348765'")
    cur = conn.cursor()
    return (conn, cur)

def getBooks():
    url = "https://www.googleapis.com/books/v1/volumes?q=9780822205104"
#    url = "https://openlibrary.org/api/books?bibkeys=ISBN:0822205106&jscmd=data&format=json"    
    response = requests.get(url)
    print(type(response.json()))
    return response.json()

@routes.get('/get')
async def getsomething(request):
#    conn, cur = await DBconn()
#    data = await request.json()
#    data = getBooks()
    return web.json_response(data)

@routes.get('/get')
async def getsomething(request):
        

if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, path="127.0.0.1", port="8080")
