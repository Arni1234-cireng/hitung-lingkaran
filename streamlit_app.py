import streamlit as st

st.title("_menghitung_ lingkaran] :rocket:")
r = st.number_input("masukan jari-jari (cm):", 0)
if st.button("hitung lingkaran", type"primary"):
L=Math.pi*(r**2)
st.succes(f"lingkaran adalah (L:.2f)
