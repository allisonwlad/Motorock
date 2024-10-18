import streamlit as st

st.set_page_config(page_title="Motorock", layout="wide", page_icon="https://lh5.googleusercontent.com/-1I_gEnK6xa4/AAAAAAAAAAI/AAAAAAAAAAA/m20AONrAkz4/s40-c-k-mo/photo.jpg")

st.markdown("""
    <style>
        .st-emotion-cache-yfhhig {
            visibility: hidden;
        }
        .st-emotion-cache-mnu3yk {
            visibility: hidden
        } 
        
    </style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Login", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
inicio_page = st.Page("src/pages/inicio.py", title="Inicio", icon=":material/thumb_up:", default=True)


pg = st.navigation(
        {
            "Conta": [login_page],
            "Inicio": [inicio_page],
        }
    )
pg.run()
