import streamlit as st
st.header("Naya Naya Form")

Firstname = st.text_input("Enter your first name:-")
Lastname = st.text_input("Enter your last name:-")
Email = st.text_input("Enter your email address:-")

upload = st.file_uploader("Upload your image:-")

Gender = st.selectbox('Gender',('Male','Female'))

st.subheader('Apne baare me tick kijiye')

pagal = st.checkbox('Pagal')
bewakoof = st.checkbox('Bewakoof')
chutiya = st.checkbox('Chutiya')

if pagal:
     st.write("Great You are a certified paagal 😆")

if bewakoof: 
     st.write("Kya bat hai aap to bewakoof nikale 😆")

if chutiya:
     st.write("Humko to malum tha ki aap chutiye ho 😆 ")

st.subheader("Ye solve karke batao to mane")
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

     

