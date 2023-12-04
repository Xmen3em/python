# This is simplest student data management program in python

class Student:

    def __init__(self, name = '', rollno = 0, m1 = 0, m2 = 0, m3 = 0, m4 = 0, m5 = 0, m6 = 0):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        self.m6 = m6
    
    def accept(self, Name,Rollno, mark_1, mark_2, mark_3, mark_4, mark_5, mark_6):
        ob = Student(Name, Rollno, mark_1, mark_2, mark_3, mark_4, mark_5, mark_6)
        ls.append(ob)
    
    def display(self, ob):
        print('name: ', ob.name)
        print('Roll number: ', ob.rollno)
        print('Mark_1: ', ob.m1)
        print('Mark_2: ', ob.m2)
        print('Mark_3: ', ob.m3)
        print('Mark_4: ', ob.m4)
        print('Mark_5: ', ob.m5)
        print('Mark_6: ', ob.m6)

    def search(self, rn):
        c = 0
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i
                c = 1
                break
        if c == 0:
            print('incorrect rollno')
                 
    
    def delete(self, rn):
        i = obj.search(rn)
        if i == None:
            return
        else:
            del ls[i]

    def update(self, rn, new_rn):
        i = obj.search(rn)
        if i == None:
             return
        else: 
            c = 0 
            for j in range(ls.__len__()):
                if new_rn == ls[j].rollno:
                    print('this rollno already exists')
                    c = 1
                    break      
            if c == 0:
                ls[i].rollno = new_rn


ls = [] 
obj = Student()   

print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")
while True:
    choise = int(input('\nenter a number (1 -> 6) : '))

    if choise == 1:
        c = 0
        name = input('please enter your name: ')
        Rollno = int(input('enetr your roll number: '))
        mark_1, mark_2, mark_3, mark_4, mark_5, mark_6 = map(int, input('enter your grades: ').split())
        for i in range(ls.__len__()):
            if Rollno == ls[i].rollno:
                print('this rollno already exists')
                c = 1
                break
        if c == 0:
            obj.accept(name, Rollno, mark_1, mark_2, mark_3, mark_4, mark_5, mark_6)

    elif choise == 2:
        print("\nList of Students\n")
        if ls.__len__() == 0:
             print('\tthere are no data')
        for i in range (ls.__len__()):
            obj.display(ls[i])
            print('\n')

    elif choise == 3:
        rn = int(input('\nenter a roll number of a student you want: '))
        if ls.__len__() == 0:
             print('\tthere are no data')
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                    s = obj.search(rn)
                    obj.display(ls[s])
            else:
                    print('incorrect rollno')
        
    elif choise == 4:
        rn = int(input('\nenter a roll number of a student you want to delete him: '))
        obj.delete(rn)
         
    elif choise == 5:
        rn, new_rn = map(int, input('\nenter the roll num you want to upadate it and the new: ').split())
        obj.update(rn, new_rn)

    elif choise == 6:
        print('\nThank You\n')
        break

    else:
        print('\nplease enter a correct choise\n')        