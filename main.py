import streamlit as st
from datetime import datetime

print("Start script: ", datetime.now())
st.title("Streamlit callbacks")

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

def go_to_step1():
    st.session_state.step = 1

def go_to_step2(name, age):
    st.session_state.info["name"] = name
    st.session_state.info["age"] = age
    if all(st.session_state.info.values()):
            st.session_state.step = 2
    else:
        st.warning("Please fill in the information")

if st.session_state.step == 1:
    st.header("Part1: Information")
    name = st.text_input("Name:", value=st.session_state.info.get("name", ""))
    age = st.text_input("Age:", value=st.session_state.info.get("age", ""))    
    st.button("Next", on_click=go_to_step2, args=(name, age))

elif st.session_state.step == 2:
    st.header("Part2: Review")    
    st.subheader("Please review the information")
    st.write("Name: ", st.session_state.info.get("name", ""))
    st.write("Age: ", st.session_state.info.get("age", ""))

    if st.button("Submit"):
        st.write("Thank you for your information")
        st.balloons()
        st.session_state.info = {}
    st.button("Back", on_click=go_to_step1)


print("End script: ", datetime.now())
