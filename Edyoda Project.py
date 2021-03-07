class Cinema:
    def __init__(self):
        print("Welcome to the Theatre.")
        self.rows=int(input("Enter the number of rows:"))
        self.columns=int(input("Enter the number of columns:"))
        print("1.Show the seats")
        print("2.Buy a ticket")
        print("3.Statistics")
        print("4.Show booked ticktes user info")
        print("0.Exit")
        self.option=int(input())
        self.details=[]
        self.bookseat=[]
        self.half=[]
        self.user_dict={}
      
        
        while True:
            if self.option==1:
                print("Cinema")
                for val in range(1,self.columns+1):
                    print("",val,end="")
                print()
                
                for i in range(1,self.rows+1):
                    print(i,end="")
                    for j in range(1,self.columns+1):
                        if (i,j) in self.bookseat:
                            print("B",end=" ")
                        else:
                            print("S",end=" ")
                    print()
                print("1.Show the seats")
                print("2.Buy a ticket")
                print("3.Statistics")
                print("4.Show booked ticktes user info")
                print("0.Exit")
                
                self.option=int(input())
     
            elif self.option==2:
                self.bookseat=input("enter the row and colums:").split(',')
                
                for val in self.bookseat:
                    self.details.append(val)
                val=self.bookseat[0]
                val2=self.bookseat[1]
                
                if int(val2)<=self.columns and int(val)<=self.rows:
                    if self.rows*self.columns<60:
                        self.firsthalf=self.rows//2
                        for fh in range(1,self.firsthalf+1):
                            self.half.append(fh)
                        if int(val) in self.half:
                            self.ticket_price=10
                        else:
                            self.ticket_price=8
                    else:
                        self.ticket_price=10
                else:
                    print("'Error' row and column are out of range")
                    break
                    
                print("The ticket price is",self.ticket_price,"$")
                self.ticket=input("You want to buy a ticket!!:(yes/no)")
                if self.ticket=="yes":
                    self.name=input("Enter your name:")
                    self.details.append(self.name)
                    self.age=int(input("Enter your age:"))
                    self.details.append(self.age)
                    self.gender=input("Enter your gender:")
                    self.details.append(self.gender)
                    self.phone_number=int(input("Enter your phone number:"))
                    self.details.append(self.phone_number)
                    
                    print("Booked Successfully!!!!")
                    self.details.clear()
                else:
                    print("Ok see you sooooon!!!!")
                    self.details.clear()
                    print("1.Show the seats")
                    print("2.Buy a ticket")
                    print("3.Statistics")
                    print("4.Show booked ticktes user info")
                    print("0.Exit")
                    
                    self.option=int(input())
                    
            elif self.option==3:
                
                print("number of ticktes purchased:",val[0])
                print("percentage of ticktes booked:",(val[0]/(self.rows*self.columns)*100),"%")
                if self.rows*self.columns>60:
                    print("Current income:$",10,"and $",8)
                else:
                    print("Current income:$",10)
                
                if self.rows*self.column>60:
                    print("Total income:$",((((self.rows//2)*self.columns)*10+(self.columns*(self.rows-self.rows//2)))*8),"$")
                else:
                    print("Total income:$",(self.rows*self.columns)*10)
                print("1.Show the seats")
                print("2.Buy a ticket")
                print("3.Statistics")
                print("4.Show booked ticktes user info")
                print("0.Exit") 
                
                self.option=int(input())
                    
            elif self.option==4:
                op = input("Enter the row and column by using comma:").split(',')
                tup = tuple(op)
                for dict in self.user_dict:
                    if deets==yup:
                        print("Name:",self.user_dict)
                        print("Gender:",self.user_dict)
                        print("Age:",self.user_dict)
                        print("Ticket price:",self.user_dict)
                        print("Phone number:",self.user_dict)
                print("1.Show the seats")
                print("2.Buy a ticket")
                print("3.Statistics")
                print("4.Show booked ticktes user info")
                print("0.Exit") 
                
                self.option=int(input())
            
            elif self.option==0:
                print("Thanks for visiting seeyou soon!!!!")
                break
            
            else:
                print("Please select the option from the given below")
                print("1.Show the seats")
                print("2.Buy a ticket")
                print("3.Statistics")
                print("4.Show booked ticktes user info")
                print("0.Exit")
                
                self.option=int(input())

Cinema()
