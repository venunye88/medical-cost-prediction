
import pickle
from fastapi import APIRouter
from usermodel import UsersData
from sklearn.preprocessing import StandardScaler

router = APIRouter()

@router.post("/predict")
async def predictMedicalCharges(usr: UsersData):

    # Does User Smokes
    if usr.Smoker == "no":
        x1_no = 1
        x1_yes = 0
    else:
        x1_no = 0
        x1_yes = 1
    
    # Get region user belongs to
    if usr.Region == "northeast":
        x0_northeast = 1
        x0_northwest = 0
        x0_southeast = 0
        x0_southwest = 0

    elif usr.Region == "northwest":
        x0_northeast = 0
        x0_northwest = 1
        x0_southeast = 0
        x0_southwest = 0
    
    elif usr.Region == "southeast":
        x0_northeast = 0
        x0_northwest = 0
        x0_southeast = 1
        x0_southwest = 0
    
    else:
        x0_northeast = 0
        x0_northwest = 0
        x0_southeast = 0
        x0_southwest = 1

    # Get users Gender
    if usr.Gender == "male":
        x2_female = 1
        x2_male = 0

    else:
        x2_female = 0
        x2_male = 1
    
    # Scale Users 
    scl = StandardScaler()
    scaled_dataset = scl.fit_transform([[usr.Children, usr.Age, usr.Bmi]])

    #Get individual scaled data
    children = scaled_dataset[0][0]
    age = scaled_dataset[0][1]
    bmi = scaled_dataset[0][2]

    data = [[x0_northeast, x0_northwest, x0_southeast, x0_southwest, x1_no, x1_yes, x2_female, x2_male, children, age, bmi]]

    #Load model to make prediction
    model = pickle.load(open("model.pkl","rb"))

    #Make prediction
    response = model.predict(data)
    print(response)

    #Return results
    return {"Predicted": round(response[0],3)}