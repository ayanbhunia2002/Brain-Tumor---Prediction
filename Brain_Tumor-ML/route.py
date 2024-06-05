from typing import Union
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import prediction

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_image(image: UploadFile = File(...)):
    print("Inside method...")

    file_content = await image.read()
    predict = prediction.get_prediction(file_content)
    print(predict)

    if predict == True:
        result = "Brain Tumor is detected"
    else:
        result = "No Brain Tumor detected."

    return {"result": result}


@app.get("/")
def read_root():
    return {"Hello": "World"}
