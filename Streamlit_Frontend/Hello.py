import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon = "🍛",
)

st.write("# Welcome to Dietary Intelligence Engineer 🍛")

st.sidebar.success("Select a setup.")

st.markdown(
    """
    A Dietary Intelligence Engineer is an web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
    You can find more details and the whole project on my [repo](https://github.com/zakaria-narjis/Diet-Recommendation-System).
    """
)
