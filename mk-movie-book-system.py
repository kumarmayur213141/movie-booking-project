print("="*40)
print("WELCOME TO MK MOVIE TICKET BOOKING ")
print("="*40)


customer_name = input("Enter Customer Name: ")


print("""\nAvailable Movies
       1. Bhoot Bangla
       2. Spider-Man: Brand New Day
       3. Musafir Cafe""")



movie_choice = input("Enter Movie choice (1-3): ")

match movie_choice:

    case "1":  
        movie = "Bhoot Bangla"
        prices = {"1": 150, "2": 210, "3": 190}

    case "2":
        movie = "Spider-Man: Brand New Day"
        prices = {"1": 120,"2": 180,"3": 220}

    case "3":
        movie = "Musafir Cafe"
        prices = {"1": 200,"2": 200,"3": 200}

    case _:
        print("Invalid Movie choice!")
        exit()

print("""\nShow Timings
       1. 09:00 - 11:40
       2. 14:00 - 16:40
       3. 21:00 - 23:40""")

show_choice = input("Enter Show choice (1-3): ")

match show_choice :
   case "1":
    show = "09:00 - 11:40"
   case "2":
    show = "14:00 - 16:40"
   case"3":
    show = "21:00 - 23:40"
   case _:
    print("Invalid Show choice!")
    exit()

price = prices[show_choice]


print("""\nSeat Types
       1. Silver (+₹0)
       2. Gold (+₹50)
       3. Platinum (+₹100)""")

seat_choice = input("Enter Seat choice (1-3): ")

match seat_choice:
   case "1":
    seat = "Silver"
    seat_charge = 0
   case "2":
    seat = "Gold"
    seat_charge = 50
   case "3":
    seat = "Platinum"
    seat_charge = 100
   case _: 
    print("Invalid Seat choice!")
    exit()


try:
    tickets = int(input("Enter Number of Tickets: "))

    if tickets <= 0:
        print("Invalid Number of Tickets!")
        exit()

except ValueError:
    print("Please enter a valid number!")
    exit()

price_per_ticket = price + seat_charge
total_amount = price_per_ticket * tickets


print(" ==========MK MOVIE TICKET==========")
print(f"""    Customer Name   :  {customer_name}
    Movie Name      :  {movie}
    Show Timing     :  {show}
    Seat Type       :  {seat}
    No. of Tickets  :  {tickets}
    Base Price      : ₹{price}
    Seat Charge     : ₹{seat_charge}
    Price/Ticket    : ₹{price_per_ticket}""")
print("="*40)
print(f"Total Amount: ₹{total_amount}")
print("="*40)
print("Thank You for Booking with MK Movie Ticket Booking System!")