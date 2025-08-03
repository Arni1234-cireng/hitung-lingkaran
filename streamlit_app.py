import streamlit as st
import math
st.title("_menghitung_ lingkaran] :rocket:")
r = st.number_input("masukan jari-jari (cm):", 0)

if st.button("hitung Lingkaran", type=primary):
L=Math.pi*(r**2)
st.success(f"lingkaran adalah (L:.2f)")
