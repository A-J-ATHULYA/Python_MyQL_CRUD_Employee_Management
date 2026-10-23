from datetime import datetime
from mysql import connector

# import datetime

class DbConnect:
    def get_connection(self):
        try:
            self.connection = connector.connect(
                host='localhost',
                user='root',
                password='Athulya@30',
                database='company_db'
            )
            return self.connection

        except Exception as e:
            return None


class EmployeeManager(DbConnect):

    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "insert into employee (name, place, mobile, email, department, salary, joining_date) values(%s, %s, %s, %s, %s, %s, %s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connect.commit()
            print("Employee added successfully")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            print(records)
        except Exception as e:
            print(e)

    def get_object(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee where id = %s"
            values =(id,)

            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            record = self.get_object(id= id)
            if record == None:
                print("Employee not found....!")
            print(record)
        except Exception as e:
            print(e)


    def delete(self, id=None):
        try:
            record = self.get_object(id=id)
            values = (id,)
            if record != None:
                query = "delete from employee where id = %s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Employee deleted successfully...")
            else:
                print("Employee not found...")
        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.cursor = self.connect.cursor()
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update employee set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Employee updated successfully.....")
            else:
                print("Employee not found.........")
        except Exception as e:
            print(e)


connect_instance = DbConnect()

#print(connect_instance.get_connection())

employee_instance = EmployeeManager()
# employee_instance.post(name = "Athulya", place = "Nooranad", mobile = "0987654321", email = "athulya@gmail.com", department = "IT", salary = 85000, joining_date = datetime.today())
# employee_instance.post(name = "Arjun", place = "Padanilam", mobile = "9987654321", email = "arjun@gmail.com", department = "Civil", salary = 80000, joining_date = datetime.today())
# employee_instance.post(name = "Abhijith", place = "Kayamkulam", mobile = "9887654321", email = "abhijith@gmail.com", department = "Finance", salary = 65000, joining_date = datetime.today())
# employee_instance.post(name = "Adhish", place = "Kottayam", mobile = "7987654321", email = "adhish@gmail.com", department = "EEE", salary = 75000, joining_date = datetime.today())
# employee_instance.post(name = "Ajayan", place = "Thamalakulam", mobile = "6987654321", email = "ajayan@gmail.com", department = "Marketing", salary = 55000, joining_date = datetime.today())
# employee_instance.get()

# employee_instance.retrieve(4)

# employee_instance.delete(5)


employee_instance.put(4, department="Mechanics")
employee_instance.retrieve(4)

employee_instance.get()