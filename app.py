from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from github import Github, Request

app = FastAPI()


@app.post('/search', status_code=status.HTTP_200_OK)
async def search(text: Request):
    try:
        git = Github()
        return JSONResponse(content=git.search(text.text), status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", host="localhost", port=3003, reload=True)