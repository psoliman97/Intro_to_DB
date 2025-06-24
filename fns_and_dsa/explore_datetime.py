from datetime import datetime, timedelta
def display_current_datetime() :
    current_date= datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
def calculate_future_date() :
      try:
        days = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        print("Future date after", days, "days will be:", future_date.strftime("%Y-%m-%d"))
      except ValueError:
        print("Please enter a valid integer.")

def main():
    print("=== Date & Time Explorer ===")
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
    