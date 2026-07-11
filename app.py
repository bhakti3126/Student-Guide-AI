import streamlit as st
from rag import read_pdf

st.set_page_config(page_title="Student Guide AI")

st.title("📚 Student Guide AI")

if st.button("Read PDF"):

    text = read_pdf("data/os_notes.pdf")

    st.write(text[:2000])