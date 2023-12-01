import streamlit as st
import pandas as pd

from common import get_or_init_state, init_state

conn = get_or_init_state("conn", st.connection("postgresql", type="sql"))
init_state("home_btm_diff", False)

mytable = conn.query("""
    select * 
    from mytable
""", ttl="5m")

st.write(f"""Change the data of 'mytable':""")
edited_df = st.data_editor(mytable, num_rows="dynamic")

diff_button = st.button("Review changes")
if diff_button:
    st.session_state["home_btm_diff"] = diff_button

if st.session_state["home_btm_diff"]:
    diff = pd.concat([edited_df,mytable]).drop_duplicates(keep=False)
    st.write("#### Current changes")
    st.write(diff)
    update = st.button("Update")
    if update:
        st.write("Sending")
        print("Sending...")

