import streamlit as st

from common import get_or_init_state

conn = get_or_init_state("conn", st.connection("postgresql", type="sql"))

# init state
st.write("""
# Data workspace app
This a simple app to manage and visualize data on the remote database.
""")

print(f"""
Rendering app...
session_state: {st.session_state}
secrets: {st.secrets}
""")

connections = st.secrets['connections']
st.write(f"""
Current connections: 
{connections}
""")

st.write(conn)

# List all tables
tables = conn.query("""
    SELECT table_catalog, table_schema, table_name 
    FROM information_schema.tables
    where table_schema = 'public'
""")
# tables = conn.query('SELECT * FROM mytable;', ttl="10m")

st.write("### Available tables")
st.dataframe(tables)
