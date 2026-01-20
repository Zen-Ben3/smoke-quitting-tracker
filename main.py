from datetime import date

quit_date = input("Enter the date you quit smoking (YYYY-MM-DD): ")
quit_date = date.fromisoformat(quit_date)

today = date.today()
days_smoke_free = (today - quit_date).days

cigs_per_day = int(input("Enter the number of cigarettes/vapes you used to smoke per day: "))
cigs_saved = days_smoke_free * cigs_per_day

cigarette_cost = float(input("Enter the cost of one cigarette/vape: "))
money_saved = cigs_saved * cigarette_cost

print(f"You have been smoke-free for {days_smoke_free} days. Keep pushing on!")
print(f"You have saved {cigs_saved} cigarettes/vapes since you quit.")
print(f"You have saved £{money_saved:.2f} since you quit.")