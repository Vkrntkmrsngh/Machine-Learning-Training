
import os
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,accuracy_score

def read_data():
    
    processed_data_path=os.path.join(os.path.pardir,'data','processed')
    train_data_path=os.path.join(processed_data_path,'train.csv')
    train_data_processed=pd.read_csv(train_data_path,index_col='RowNumber')

    X=train_data_processed.iloc[:,:-1]
    y=train_data_processed.iloc[:,-1]

    return train_test_split(X,y,test_size=0.2,random_state=0)

def standard_scaling(X_train,X_test):
    sc=StandardScaler()

    return sc.fit_transform(X_train),sc.fit_transform(X_test)

def model_training(X_train,y_train,X_test,algo_name,save_model=False):
    model_file_name='customer_predictor_'+algo_name+'_model.pkl'
    model_path=os.path.join(os.path.pardir,'models')
    model_file_path=os.path.join(model_path,model_file_name)
    
    if algo_name == 'LogisticRegression':
        model=LogisticRegression()
        model.fit(X_train,y_train)
        y_predicted=model.predict(X_test)
        
        if save_model:
            model_file_pickle=open(model_file_path,'wb')
            pickle.dump(model,model_file_pickle)
            model_file_pickle.close()
        
        
    elif algo_name == 'RandomForest':
        print('Inside Randomforest')
        model=RandomForestClassifier(n_estimators=10 ,random_state=0)
        model.fit(X_train,y_train)
        y_predicted=model.predict(X_test)
        print('Done modeling of Randomforest')
        print(model_file_path)
        if save_model:
            model_file_pickle=open(model_file_path,'wb')
            pickle.dump(model,model_file_pickle)
            model_file_pickle.close()
        print('Done saving model')
       
    return y_predicted

def model_evaluation(y_test,y_predicted,algo_name):
    if algo_name == 'LogisticRegression':
        confusion_metric=confusion_matrix(y_test,y_predicted)
        accuracy_value=accuracy_score(y_test,y_predicted)
        
    elif algo_name == 'RandomForest':
        confusion_metric=confusion_matrix(y_test,y_predicted)
        accuracy_value=accuracy_score(y_test,y_predicted)
        
    return confusion_metric,accuracy_value



if __name__=='__main__':
    X_train,X_test,y_train,y_test=read_data()
    X_train,X_test=standard_scaling(X_train,X_test)
    algo_name=input('Please Provide Algorithm Name to apply on data')
    y_predicted=model_training(X_train,y_train,X_test,algo_name,save_model=True)
    confusion_value,accuracy_value= model_evaluation(y_test,y_predicted,algo_name)
    print(confusion_value)
    print(accuracy_value)
