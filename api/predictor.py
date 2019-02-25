import pickle
import pandas as pd
import numpy as np

class agent_predictor():
  def __init__(self):
    pass
  
  def deserialize(self):
    # de-serialize mlp_nn.pkl file into an object called model using pickle
    with open('customer_predictor_model.pkl', 'rb') as handle:
        model = pickle.load(handle)
        return model
  
  def predict(self, creditscore, geography, gender,age,tenure,balance,hascrcard,isactivemember,estimatedsalary):
    model = self.deserialize()
    return model.predict(np.array([[creditscore, geography, gender,age,tenure,balance,hascrcard,isactivemember,estimatedsalary]]))
