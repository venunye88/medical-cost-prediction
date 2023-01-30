from fastapi import FastAPI

app = FastAPI()

@app.post('/predict')
async def predictMedicalCharges():
    pass