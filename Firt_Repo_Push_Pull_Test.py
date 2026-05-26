try:
    visitor = input("Ask the current session of the day: ").strip().lower()
except EOFError:
    visitor = ""

if visitor == "morning":
    print("Good Morning")
else:
    print("Have a nice day")