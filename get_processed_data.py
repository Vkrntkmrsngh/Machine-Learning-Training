
import numpy as np
import pandas as pd
import os

#o read data from raw folder
def read_data():
    #set the path of the raw data
    raw_data_path=os.path.join(os.path.pardir,'data','raw')
    train_data_path=os.path.join(raw_data_path,'train.csv')
    test_data_path=os.path.join(raw_data_path,'test.csv')
    
    #read data file with all default calumns
    train_data=pd.read_csv(train_data_path,index_col='RowNumber')
    test_data=pd.read_csv(test_data_path,index_col='RowNumber')
    
    #Create a column in test data so that we can merge this with train data and later we can saperate it.#Create 
    test_data['Exited']=-999
    
    #concatenate train and test data to perform operation on both
    total_data=pd.concat((train_data,test_data),axis=0)
    
    return total_data

#to process the data
def process_data(df):
    #using the method chaining concept
    return(df
           #working with missing values
           .pipe(fill_missing_values)
           #replacing outliers
           .pipe(replace_outliers)
           #creating dummies for categorical features
           .pipe(pd.get_dummies,columns=['Geography','Gender'])
           #drop useless columns
           .drop(['CustomerId','Surname'],axis=1)
           #reorder columns
           .pipe(reorder_columns)
            )

def reorder_columns(df):
    columns=[column for column in df.columns if column!='Exited']
    columns=columns+['Exited']
    df=df[columns]
    return df


def fill_missing_values(df):
    #creditscore
    mean_credit_score=df.CreditScore.mean()
    df.CreditScore.fillna(mean_credit_score,inplace=True)
    
    #age
    mean_age=df.CreditScore.mean()
    df.Age.fillna(mean_age,inplace=True)
    return df

def replace_outliers(df):
    mean_credit_female=df[df.Gender=='Female'].CreditScore.mean()
    
    #Replacing outliers#Replaci 
    df['CreditScore'].replace([1100,1050], mean_credit_female,inplace=True) 
    return df

#To write data in processed folder
def write_data(df):
    processed_data_path=os.path.join(os.path.pardir,'data','processed')
    write_train_path=os.path.join(processed_data_path,'train.csv')
    write_test_path=os.path.join(processed_data_path,'test.csv')

    #train data
    df.loc[df.Exited!=-999].to_csv(write_train_path)
    #test data
    columns=[column for column in df.columns if column!='Exited']
    df.loc[df.Exited==-999,columns].to_csv(write_test_path)


if __name__=='__main__':
    df=read_data()
    df=process_data(df)
    write_data(df)
