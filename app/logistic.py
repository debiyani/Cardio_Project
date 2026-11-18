# import streamlit as st
# from app.model

# st.header('Cardiovascular Disease Prediction')
# st.subheader('Using :red[Logistic] :blue[Regression]')

# # feature train garda jasto haleko hunxa testai serially halne
# age = st.slider(
#     'Age',
#     min_value=28,
#     max_value=65,
#     value=35,
#     step=1
# )

# gender_dict = {1:'Female', 2:'Male'}

# gender = st.sidebar.radio( #selectbox for dropdown
#     'Gender',
#     options=gender_dict.keys(),
#     format_func=lambda x : gender_dict.get(x)
# )

# height = st.sidebar.slider(
#     'Height', min_value=150, max_value=190, value =160
# )

# weight = st.sidebar.slider(
#     'Weight', min_value=45, max_value=110, value =120
# )

# ap_hi = st.sidebar.slider(
#     'Systolic Pressure', min_value=90, max_value = 180, value=120
# )

# ap_lo = st.sidebar.slider(
#     'DiSystolic Pressure', min_value=50, max_value = 90, value=80
# )

# cholesterol_dict = {
#     1:'Low Cholestrol',
#     2:'Mild Cholestrol',
#     3:'High Cholestrol'
# }

# cholesterol = st.sidebar.radio(
#     'Cholesterol', options=cholesterol_dict.keys(),
#     format_func=lambda x : cholesterol_dict.get(x)
# )

# gluc_dict = {
#     1:'Low Glucose',
#     2:'Mild Glucose',
#     3:'High Glucose'
# }

# gluc = st.sidebar.radio(
#     'Glucose', options=gluc_dict.keys(),
#     format_func=lambda x : gluc_dict.get(x)
# )

# smoke_dict = { 0: 'Doesnot Smoke', 1:'Does Smoke'}
# smoke = st.sidebar.radio(
#     'Smoke', options=smoke_dict.keys(), format_func = lambda x : smoke_dict.get(x)
# )

# alco_dict = {0:'Doesnot Drink', 1:'Does Drink'}
# alco = st.sidebar.radio(
#     'Alcohol', options= alco_dict.keys(), format_func=lambda x : alco_dict.get(x)
# )

# active_dict = {0:'Does do PA', 1:'Doesnot do PA'}
# active = st.sidebar.radio(
#     'Physical Activities (PA)', options=active_dict.keys(), format_func=lambda x: active_dict.get(x)
# )