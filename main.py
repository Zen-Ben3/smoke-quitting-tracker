from datetime import date

quit_date = input("Enter the date you quit smoking (YYYY-MM-DD): ")
quit_date = date.fromisoformat(quit_date)

today = date.today()
days_smoke_free = (today - quit_date).days

print(f"You have been smoke-free for {days_smoke_free} days. Keep pushing on!")
