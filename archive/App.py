import streamlit as st
from auth import login, register

st.set_page_config(
    page_title="ASL Recognition System",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN PAGE
if not st.session_state.logged_in:

    menu = st.sidebar.selectbox(
        "Select",
        ["Login","Register"]
    )

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if menu == "Login":

        if st.button("Login"):

            user = login(
                username,
                password
            )

            if user:
                st.session_state.logged_in = True
                st.success("Login Successful")
                st.rerun()

            else:
                st.error("Invalid Login")

    else:

        if st.button("Register"):

            if register(
                username,
                password
            ):

                st.success("Registered")

            else:

                st.error(
                    "User already exists"
                )

# DASHBOARD
else:

    st.sidebar.success(
        "Logged In"
    )

    page = st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "Detection",
            "History"
        ]
    )

    if page == "Home":

        st.title(
            "🤟 ASL Recognition System"
        )

        st.write(
            "Welcome to Dashboard"
        )

    elif page == "Detection":

        st.header(
            "Live Detection"
        )

        st.info(
            "Run realtime_detection.py"
        )

    elif page == "History":

        st.header(
            "Prediction History"
        )

    if st.sidebar.button(
        "Logout"
    ):

        st.session_state.logged_in = False
        st.rerun()