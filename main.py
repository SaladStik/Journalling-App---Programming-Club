import json
import os

# Define file to store journal entries
FILE_NAME = "journal_entries.json"

# Initialize entries
entries = {}

# Check if the journal file exists and load it if available
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        entries = json.load(file)
else:
    entries = {}

# Main loop
while True:
    print("\n--- Journal App ---")
    print("1. Create new entry")
    print("2. Edit existing entry")
    print("3. View all entries")
    print("4. Quit")

    choice = input("Choose an option: ")

    match choice:
        case "1":  # Create new entry
            title = input("Enter the title of your journal entry: ")
            content = input("Enter your journal entry content: ")
            entries[title] = content
            print(f"\n\nJournal entry '{title}' created.")

        case "2":  # Edit existing entry
            title = input("\n\nEnter the title of the journal entry to edit: ")
            if title in entries:
                print(f"\n\nCurrent content: {entries[title]}")
                new_content = input("Enter the new content for this entry: ")
                entries[title] = new_content
                print(f"\n\nJournal entry '{title}' updated.")
            else:
                print(f"\n\nEntry '{title}' not found.")

        case "3":  # View all entries
            if entries:
                print("Your journal entries:")
                for title, content in entries.items():
                    print(f"\n\n- {title}: {content[:50]}{'...' if len(content) > 50 else ''}")
            else:
                print("No journal entries found.")

        case "4":  # Quit
            with open(FILE_NAME, "w") as file:
                json.dump(entries, file, indent=4)
            print("Goodbye!")
            break

        case _:  # Default case for invalid options
            print("Invalid option, please try again.")
