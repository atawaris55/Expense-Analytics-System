#   P6 expenses tracker



class Expenses:

    def add_expense(self):
        with open("expenses.txt", 'a') as file:
            amount = int(input("Enter the amount you spend: "))

            print("Select category:-")
            print("1. Electronics\n2. Clothing\n3. Food\n4. Books\n5. Grocery")
            category_choice = int(input("Enter the category choice: "))

            categories = {
                1: "Electronics",
                2: "Clothing",
                3: "Food",
                4: "Books",
                5: "Grocery"
            }

            if category_choice not in categories:
                print("Invalid choice")
                return

            category = categories[category_choice]

            date = int(input("Enter Date: "))

            print("Select Month:-")
            print("1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. July\n8. August\n9. September\n10. October\n11. November\n12. December")

            month_choice = int(input("Enter the Month: "))

            months = {
                1: "January", 2: "February", 3: "March", 4: "April",
                5: "May", 6: "June", 7: "July", 8: "August",
                9: "September", 10: "October", 11: "November", 12: "December"
            }

            if month_choice not in months:
                print("Invalid Month")
                return

            month = months[month_choice]

            file.write(f"{amount},{category},{date},{month}\n")

        print("\nExpense Added Successfully!")                   

    def see_expense(self):
        try:
            with open("expenses.txt",'r') as file:
                print("--All expenses--")
                for line in file:
                    amount,category,date,month=line.strip().split(',')
                    print(f"{amount},{category},{date},{month}")
        except FileNotFoundError:
            print("No data found!")
    
    def month_total(self):
        total1={}
        try:
            with open("expenses.txt",'r') as file:
                for line in file:
                    amount,_,_,month=line.strip().split(',')
                    if month in total1:
                        total1[month]+=int(amount)

                    else:
                        total1[month]=int(amount)
            print("\n--monthwise total--")
            for mon,amt in total1.items():
                print(mon,':',amt)
        except FileNotFoundError:
            print("data not found!")    

    def category_total(self):
        total2={}
        try:
            with open("expenses.txt",'r') as file:
                for line in file:
                    amount,category,_,_=line.strip().split(",")
                    if category in total2:
                        total2[category]+=int(amount)

                    else:
                        total2[category]=int(amount)
                    
            print("\n--Categorywise total--")
            for cat,amt2 in total2.items():
                print(cat,":",amt2)

        except FileNotFoundError:
            print("data not found")   
         
user=Expenses()
while True:
        print("\nPress 1 for Add expenses")
        print("Press 2 for View expenses")
        print("Press 3 to show Total")
        print("Press 4 for Category wise total")
        print("Press 5 for Exit")

        choice=int(input("Enter your choice: "))

        if choice==1:
            user.add_expense()

        elif choice==2:
            user.see_expense()
        
        elif choice==3:
            user.month_total()

        elif choice==4:
            user.category_total()

        elif choice==5:
            print("\n--You Exited from Expense Tracker!--")
            break

        else:
            print("INVALID CHOICES!!")