class Student(): 


    # constructer 
    def __init__(self) : 
        name = ''
        age = 12
        house = ''  
        equipment = 'pencil' 
        bagcolor = 'red' 

    # function 
    def change_details(self):
            self.age = input('please enter your age : ')
            self.name = input('please enter your name : ')
            self.house = input('please enter your house address : ')
            self.equipment = input('please enter your equipment : ')
            self.bagcolor = input('please enter your bagcolor : ')
            

    def show_details(self):   
            print('the details of students are ')  
            print('Name : ' ,self.name) 
            print('age : ' ,self.age) 
            print('bagcolor : ' ,self.bagcolor) 
            print('house : ' ,self.house) 
            print('equipment : ' ,self.equipment)


#object  
John = Student() 
John.change_details() 
John.show_details()
arinjay = Student()  
arinjay.change_details() 
arinjay.show_details()



        
        