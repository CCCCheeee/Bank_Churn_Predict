
import streamlit as st
import pandas as pd 
import numpy as numpy
import pickle



st.write("""
# Bank Churn Prediction

""")

st.sidebar.header('User input')

def user_input_features():
    side=st.sidebar
    male=0
    female=0
    france=0
    germany=0
    spain=0
    diamond=0
    gold=0
    platinum=0
    silver=0
    
    age=side.slider("Age",0,110,0)
    tenure=side.slider("Tenure",0,100,0)
    satisfaction=side.slider("Satisfaction Score",0,5,3)

    credit_score=side.number_input("Credit score",min_value=0)
    balance=side.number_input("Balance",min_value=0.00)
    num_product=side.number_input("Number of Products",min_value=0)
    salary=side.number_input("Estimated Salary",min_value=0.00)

    has_card=side.selectbox('Has Credit Card?',('Yes','No'))
    if has_card=='Yes':
        hcard=1
    else:
        hcard=0
    #st.write('card',hcard)
    
    is_active=side.selectbox('Is Active Member?',('Yes','No'))
    if is_active=='Yes':
        active=1
    else:
        active=0
    #st.write('active',active)

    complain=side.selectbox('Has Complain?',('Yes','No'))
    if complain=='Yes':
        ccomplain=1
    else:
        ccomplain=0
    #st.write('complain',ccomplain)
    
    gender=side.selectbox('Gender',('Male','Female'))
    if gender == 'Male':
        male=1
    else:
        female=1 
    #st.write('male',male,'\n','female',female)
    geography=side.selectbox('Geography',('France','Germany','Spain'))
    if geography =='France':
        france=1
    elif geography =='Germany':
        germany=1
    else:
        spain=1
    #st.write('f',france, 'g',germany,'s',spain)
    card_type=side.selectbox('Card Type',('Diamond','Gold','Silver','Platinum'))
    if card_type =='Diamond':
        diamond=1
    elif card_type=='Gold':
        gold=1
    elif card_type=='Silver':  
        silver=1
    else:
        platinum=1 
    
    #st.write('d',diamond, 'g',gold,'s',silver,'p',platinum)

    data={'cscore':credit_score,
                          'age':age,'tenure':tenure,
                          'balance':balance,
                          'num_product':num_product,
                          'hcard':hcard,'active':active,
                          'salary':salary,'complain':ccomplain,
                          'satisfaction':satisfaction,'female':female,
                           'male': male,'france':france,'germany':germany,
                           'spain':spain,'diamond':diamond,'gold':gold,
                           'platinum':platinum,'silver':silver}
    features=pd.DataFrame(data,index=[0])
    st.subheader('Input Parameter')
    st.write(features)
    return features

 
df= user_input_features()

#read model
svm=pickle.load(open('bank_churn_v1.pkl','rb'))
prediction=svm.predict(df)



st.subheader('Predict Result')
st.write('The result is:',prediction[0])
st.write(prediction)



st.subheader("Target Name")
data1={'Exited':1,'Not Exited':0}
target=pd.DataFrame(data1,index=[0])
st.write(target)

