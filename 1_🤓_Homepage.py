# Modules
import pyrebase
import streamlit as st
import requests
from datetime import datetime

# Configuration Key
firebaseConfig = {
    'apiKey': "AIzaSyBYL_QHbdMv_Bhgf5POx4A2E-fHRndkRw8",
    'authDomain': "splitmyaudio2.firebaseapp.com",
    'projectId': "splitmyaudio2",
    'databaseURL': "https://splitmyaudio2-default-rtdb.europe-west1.firebasedatabase.app/",
    'storageBucket': "splitmyaudio2.appspot.com",
    'messagingSenderId': "763028572860",
    'appId': "1:763028572860:web:9bbe75d2cf5544d4791eb9",
    'measurementId': "G-C4RS07ETKH"
}

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()


def main(user: object):
    st.write(f"You're logged in as {st.session_state['user']['email']}")

    set_code(code=user['refreshToken'])

    st.write("Hello World")
    st.code(st.session_state.user)
    st.button('Logout')
    if st.button:
        logout()
        print('logout clicked')


def set_code(code: str):
    st.experimental_set_query_params(code=code)


def login_form(auth):
    print('login form def')
    email = st.text_input(
        label="email", placeholder="fullname@gmail.com")
    password = st.text_input(
        label="password", placeholder="password", type="password")

    if st.button("login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state['user'] = user
            st.experimental_rerun()
        except requests.HTTPError as exception:
            st.write(exception)
            st.code(st.session_state.user)


def logout():
    del st.session_state['user']
    st.experimental_set_query_params(code="/logout")


def get_user_token(auth, refreshToken: object):
    user = auth.get_account_info(refreshToken['idToken'])

    user = {
        "email": user['users'][0]['email'],
        "refreshToken": refreshToken['refreshToken'],
        "idToken": refreshToken['idToken']
    }

    st.session_state['user'] = user

    return user


def refresh_session_token(auth, code: str):
    try:
        return auth.refresh(code)
    except:
        return "fail to refresh"


# authentication

if "user" not in st.session_state:
    st.session_state['user'] = None

if st.session_state['user'] is None:
    try:
        code = st.experimental_get_query_params()['code'][0]

        refreshToken = refresh_session_token(auth=auth, code=code)

        if refreshToken == 'fail to refresh':
            raise ValueError

        user = get_user_token(auth, refreshToken=refreshToken)

        main(user=user)
    except:
        st.title("Login")
        login_form(auth)

else:
    main(user=st.session_state['user'])
