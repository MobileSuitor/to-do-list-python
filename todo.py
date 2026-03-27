# This program will allow the user to create and manipulate a to-do list
# Functions: viewing tasks, adding tasks, removing tasks, marking task as completed
# Consider adding the following features:
#   - dictionary for menu
#   - f string to assign numbers to tasks (task list breaks when adding/removing)
#   - undo feature?
#   - clear all tasks feature
#   - add feature that saves list in between runs

to_do_list = ["1. Email WWU and send transcripts",
         "2. Fix wiper arm",
         "3. Buy flight tickets for May",
         "4. Pull money out of Thrivent account"]

# Define a function that prints task list for user
def view_tasks():
    print(*to_do_list, sep='\n')
    # variable that counts items in list
    task_count = len(to_do_list)
    print("\nYou have ", task_count, " tasks remaining.")

# Define a function that adds tasks to the end of the list
def add_task():
    # get user input for new task
    task_input = input("\nEnter a task to add: ")
    # append user input to task list
    to_do_list.append(task_input)
    print(*to_do_list, sep='\n')

# Define a function that removes a task
def remove_task():
    # get user input for task to be removed
    removed_task = int(input("\nEnter the number of the task you'd like to remove: "))
    # subtract 1 from removed_task input to select correct index
    removed_task = removed_task - 1
    to_do_list.pop(removed_task)
    print(*to_do_list, sep='\n')

# Define a function that marks a task as complete
def complete_task():
    # get user input for task to be marked
    task_done = int(input("\nEnter the number of the completed task: "))
    # subtract 1 from task_done to select correct index
    task_done = task_done - 1
    to_do_list[task_done] += '   \u2714'
    print(*to_do_list, sep='\n')


# Define a function that prints a menu
def print_menu():
    print("\n")
    print(30 * "-", "MENU", 30* "-")
    print("1. Add task to list")
    print("2. Remove task from list")
    print("3. Mark task as completed")
    print("4. View tasks")
    print("5. Exit")
    print(67 * "-")

# create a menu loop that prompts user for input based on
# the function they want to call (add a task, remove a task, mark as complete)
# consider using dictionary for future menu iteration
def option_one():
    print("Executing option one...")
    input("Press Enter to continue...\n")
    add_task()

def option_two():
    print("Executing option two...")
    input("Press Enter to continue...\n")
    remove_task()

def option_three():
    print("Executing option three...")
    input("Press Enter to continue...\n")
    complete_task()

def option_four():
    print("Executing option four...")
    input("Press Enter to continue...\n")
    view_tasks()

def main():
    while True:
        print_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            option_one()
        elif choice == "2":
            option_two()
        elif choice == "3":
            option_three()
        elif choice == "4":
            option_four()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Please input a valid choice.")


# verify view_tasks function works
#view_tasks()

# verify add_task function works
# add_task()

# verify remove_task function works
# remove_task()

# verify complete_task function works
# complete_task()

# verify print_menu function works
# print_menu()

# verify main() function works
main()