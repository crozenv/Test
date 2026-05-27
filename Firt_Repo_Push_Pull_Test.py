try:
    visitor = input("Ask the current session of the day: ").strip().lower()
except EOFError:
    visitor = ""

if visitor == "morning":
    print("Good Morning")
elif visitor == "Afternoon":
    print("Good Afternoon")
else:
    print("Have a nice day")
    print("Time for TVK")