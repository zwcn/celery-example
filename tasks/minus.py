from app import app


@app.task
def minus(x, y):
    return x - y
