import uvicorn


#mongodb+srv://vbucaj:Daors%40$$$2021@cluster0.zeg1h.mongodb.net/<db>?retryWrites=true&w=majority


if __name__=='__main__':
    uvicorn.run('server.app:app',host="0.0.0.0", port=8080, reload=True)