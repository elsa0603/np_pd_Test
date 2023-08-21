import numpy as np
import pandas as pd
import streamlit as st

st.title("測試 numpy/pandas")
a = np.array([89,71,69,77,63,85,92])
b = st.number_input("輸入成績：", key="num_b")

if st.button("輸入完成"):
    a = np.append(a, b)
    st.write(a)
    