import requests

def encode(var=str, values=str):
        """
        Encode a variable
        """
        try:
            data = {"Gender": ("Male, Female"),
                    "Marriage": ("Married", "Single", "Other"),
                    "Education": ("Graduate School","University", "High School", "Others")}
            if var == "Gender":
                return data["Gender"].index(values)
            return data[var].index(values) + 1
        except:
             return
        
def predict(features):
     """
     Predict the default risk
     """

     URL = "https://default-prediction-l17p.onrender.com"
     req = requests.get(URL)
     if req.status_code != 200:
          return "Error: Unable to connect to the server!"
     URL += "/predict"
     result = requests.post(URL, json={"data": [features]})
     return result.json()