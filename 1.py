import streamlit as st

def my_function(x):
    return x**2

st.title("Пример вызова функции")

num = st.number_input("Введите число", value=2)
if st.button("Вычислить квадрат"):
    result = my_function(num)
    st.write(f"Результат: {result}")