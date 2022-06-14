from dataclasses import dataclass
from tinydb import TinyDB, Query
import pandas as pd
import streamlit as st


@dataclass
class Customer:
    customer_id: int
    customer_name: str
    customer_address: str
    customer_tax_no: str


# database locations
db_name = 'customer_master'
db_location = ''
# create database
db = TinyDB(db_location + db_name + '.json')

# table name
table_name = 'customer_table'
# create table class
table = db.table(table_name)

# Streamlit app
st.title('Customer Master')

table_json = table.all()
df = pd.DataFrame(table_json)#.sort_values(by=['customer_id'])

st.header('Enter customer details here:')
customer_id_input = st.text_input('Customer ID:', value="")
customer_name_input = st.text_input('Name:', value="")
customer_address_input = st.text_input('Address:', value="")
customer_tax_no_input = st.text_input('Tax Number:', value="")

if st.button('Submit'):
    customer = Customer(customer_id_input, customer_name_input, customer_address_input, customer_tax_no_input)
    # insert single item
    new_item = {"customer_id": customer.customer_id,
                "customer_name": customer.customer_name,
                "customer_address": customer.customer_address,
                "customer_tax_no": customer.customer_tax_no,
                }
    table.insert(new_item)
    st.write("Success 👋")
    st.write('Written to database')
    st.write(customer)
    st.experimental_rerun()

st.header('Customers List')
st.write('Sorted by customer id')
st.table(df)
