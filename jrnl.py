import json

VERSION = "0.1"

# Create a dictionary to store the work sessions
jrnl_sessions = {}

# Load the existing work sessions from the json file, if it exists
try:
    with open('jrnl_sessions.json') as f:
        jrnl_sessions = json.load(f)
except FileNotFoundError:
    pass

# Prompt the user to choose an option
choice = input("[A]dd or [S]ummary Mode?: ")

# If the user chose to add a work session, prompt for the category and duration
if choice.lower() == "a":
    while True:
        category = input("Category (or 'e' to quit): ")

        # If the user entered 'exit', break out of the loop
        if category.lower() == "e":
            break

        duration = int(input("Duration (mins): "))

        # If the category is not in the dictionary, add it with the duration as the value
        if category not in jrnl_sessions:
            jrnl_sessions[category] = duration
        # If the category is already in the dictionary, add the duration to the existing value
        else:
            jrnl_sessions[category] += duration

# If the user chose to see the summary, print the work sessions in descending order of duration
elif choice.lower() == "s":

    total_duration = sum(jrnl_sessions.values())

    total_duration_hrs = int(total_duration / 60)

    print("""
    ___   _______   _____  ___   ___       
    |"  | /"      \ (\"   \|"  \ |"  |      
    ||  ||:        ||.\\   \    |||  |      
    |:  ||_____/   )|: \.   \\  ||:  |      
___|  /  //      / |.  \    \. | \  |___   
/  :|_/ )|:  __   \ |    \    \ |( \_|:  \  
(_______/ |__|  \___) \___|\____\) \_______)                                              
"""+ "v" + VERSION + "\tBy Will D" + "\n\n—————————————————————————————")

    # Calculate the total duration of all work sessions
    total_duration = sum(jrnl_sessions.values())

    for key, value in sorted(jrnl_sessions.items(), key=lambda item: item[1], reverse=True):
        # Calculate the percentage of time spent on this category
        percentage = round(value / total_duration * 100, 2)
        print(f"{key:10} {value:>4} mins ({percentage}%)")
    print("—————————————————————————————\n" + f"TOTAL {total_duration:>9} mins / {total_duration_hrs} hrs\n" + "—————————————————————————————\n")

# If the user entered an invalid choice, let them know
else:
    print("Invalid choice. Please try again.")

# Save the work sessions to a json file
with open('jrnl_sessions.json', 'w') as f:
    json.dump(jrnl_sessions, f)
