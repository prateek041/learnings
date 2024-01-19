## Installing FastAPI

> pip install "fastapi[all]"

## First Steps

Create a basic FastAPI api.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/"):
def root():
    return {"Message": "Hello World"}
```

- @app.get("/") is a decorator 
