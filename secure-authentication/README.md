# Streamlit-Authenticator

A secure authentication module to validate user credentials in a Streamlit application.

## YAML configuration file 
Initially create a YAML configuration file and define your users' credentials (names, usernames, and plain text passwords). In addition, enter a name, random key, and number of days to expiry for a JWT cookie that will be stored on the client's browser to enable passwordless reauthentication. If you do not require reauthentication, you may set the number of days to expiry to 0.
```
credentials:
  names: ['John Smith', 'Rebecca Briggs']
  usernames: ['jsmith', 'rbriggs']
  passwords: ['123', '456'] # To be replaced with hashed passwords
cookie:
  name: 'some_cookie_name'
  key: 'some_signature_key'
  expiry_days: 30
```
Then use the Hasher module to convert the plain text passwords into hashed passwords.
```
hashed_passwords = stauth.Hasher(['123', '456']).generate()
```
Finally replace the plain text passwords in the configuration file with the hashed passwords.