import streamlit as td
import  requests 
from bs4 import BeautifulSoup
import pandas as pd

def get_data(dept):
    url = requests.get(f'https://www.{dept}.ruet.ac.bd/teacher_list').text
    soup = BeautifulSoup(url, 'lxml')
    teachers = soup.find_all('tr')[1:]
    name_en = []
    designation = []    
    phone_no = []
    email = []
    dept=[]
    for teacher in teachers:
        name = teacher.find_all('td')[1].text.strip()
        desig = teacher.find_all('td')[3].text.strip()
        phone = teacher.find_all('td')[6].text.strip()
        em = teacher.find_all('td')[5].text.strip()
        dept = teacher.find_all('td')[4].text.strip()

        name_en.append(name)
        designation.append(desig)
        phone_no.append(phone)
        email.append(em)
        dept.append(dept)

    data = pd.DataFrame({'Name': name_en, 'Designation': designation, 'Phone': phone_no, 'Email': email, 'Department': dept})
    return data
def main():
    td.title("RUET Teacher Information")
    #department selection
    dept = td.selectbox ['eee', 'chem', 'math', 'phy', 'chem']
    dept =  st.sidebar.selectbox("Select Department", dept ).lower()

    if dept:
        data = get_data(dept)
        st.dataframe(data)

        #constructor