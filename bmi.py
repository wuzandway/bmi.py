import streamlit as st
def bmi(w, h):
    return w/(h*h)

w =st.number_input('請輸入體重(KG)？')
h =st.number_input('請輸入身高(M)？')

comfilm_input=st.comfilm_input("OK")
if comfilm_input:
    bmi = bmi(w, h)
    st.writ('BMI為', bmi)
    if (bmi < 18):
        st.writ('體重過輕')
    elif (bmi < 24):
        st.writ('體重正常')
    elif (bmi < 27):
        st.writ('體重過重')
    else:
        st.writ('體重肥胖')
