import streamlit as st


from Employee_views import EmployeeManager

employee_instance = EmployeeManager()

tab1, tab2 = st.tabs(["ADD", "VIEW"])

with tab1:
    st.header("Add New Employee")

    Name  = st.text_input("Enter Name :")
    Place  = st.text_input("Enter Place :")
    Phone  = st.text_input("Enter Contact Number :")
    Email  = st.text_input("Enter Email :")
    Department = st.text_input("Enter Department:")
    Salary  = st.text_input("Enter Salary :")
    Joining_date  = st.text_input("Enter Joining Date :")
    if st.button("Add New Employee"):
        employee_instance.post(name = Name, place = Place, mobile = Phone, email = Email, department = Department, salary = Salary, joining_date = Joining_date)
        st.success("New Employee Added Successfully")
with tab2:
    st.header("View Old Employees")


