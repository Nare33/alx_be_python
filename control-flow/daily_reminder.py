def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time_bound? (yes/no): ")

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. consider tackling it soon.")
                case "medium":
                    if time_bound == "yes":
                        print(f"Reminder: '{task}' is a medium priority task. Aim to complete it by today.")
                    else:
                        print(f"Reminder: '{task}' is a medium priority task. Try to allocate time for it.")
                        case "low":
                            if time_bound == "yes"
                            print(f"Reminder: '{task}' is a low priority task. Consider it if you have extra time today.")
                        else:
                            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
                            case _:
                                print("Invalid priority level.")

                                if __name__ == "__main__":
                                    main()
