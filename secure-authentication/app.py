import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml import SafeLoader

# hashed_passwords = stauth.Hasher(['smith', 'black']).generate()

# import the configuration file into your script and create an authentication object.

with open('config.yml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials']['names'],
    config['credentials']['usernames'],
    config['credentials']['passwords'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Render the login module as follows.
# Here you will need to provide a name for the login form, and specify where the form should be located i.e. main body or sidebar (will default to main body).

name, authentication_status, username = authenticator.login('Login', 'main')

# You can then use the returned name and authentication status to allow your verified user to proceed to any restricted content.
# In addition, you have the ability to add an optional logout button at any location on your main body or sidebar (will default to main body)

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif not authentication_status:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')

# Should you require access to the persistent name, authentication status, and username variables, you may retrieve them through Streamlit's session state
# using st.session_state["name"], st.session_state["authentication_status"], and st.session_state["username"].
# This way you can use Streamlit-Authenticator to authenticate users across multiple pages.

# if st.session_state["authentication_status"]:
#     authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif not st.session_state["authentication_status"]:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] is None:
#     st.warning('Please enter your username and password')
