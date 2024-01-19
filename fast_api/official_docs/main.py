from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class EnumTest(str, Enum):
    first = "first"
    second = "Second"


@app.get("/testing/{item}")
async def root(item: int):
    return {"Message": item}


@app.get("testing/enum/{enum_value}")
def testing_enum(enum_value: EnumTest):
    return {"Message": enum_value}
