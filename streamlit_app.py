import streamlit as st

st.title("Halaman Redirect")
if st.button("Daftar Sekarang"):
    st.markdown("[Klik jika tidak otomatis redirect](https://situsdontoto7.space/register?inviteCode=vtgrVp7)")
    st.write('<meta http-equiv="refresh" content="0;url=https://situsdontoto7.space/register?inviteCode=vtgrVp7">', unsafe_allow_html=True)
