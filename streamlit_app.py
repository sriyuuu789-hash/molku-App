import streamlit as st

st.title("Project LPK 2026")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")
1+1=2
st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)
