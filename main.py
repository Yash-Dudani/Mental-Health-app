from models import User
from test import MentalHealthTest
from history import History

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = User(name, email, password)
            result = user.save()

            if result == "email_exists":
                print("❌ This email is already registered! Try logging in.")
            elif result == "invalid_email":
                print("❌ Please enter a valid email address.")
            elif result == "success":
                print("✅ Registration successful! Now log in to continue.")
            else:
                print("❌ Registration failed due to a database error.")

        elif choice == "2":
            email = input("Enter email: ")
            password = input("Enter password: ")
            user_data = User.login(email, password)

            if user_data:
                print(f"\nWelcome, {user_data[1]}!")
                user_id = user_data[0]
                user = User("", "", "") 

                while True:
                    print("\n1. Take Mental Health Test\n2. View Test History\n3. Logout\n4. Delete Account")
                    option = input("Choose an option: ")

                    if option == "1":
                        test = MentalHealthTest(user_id)
                        test.conduct_test()

                    elif option == "2":
                        history = History(user_id)
                        history.show_history()

                    elif option == "3":
                        print("👋 Logged out successfully!")
                        break

                    elif option == "4":
                        confirm = input("⚠️ Are you sure you want to delete your account? (yes/no): ")
                        if confirm.lower() == "yes":
                            user.delete_account(user_id)
                            break  
                        else:
                            print("Account deletion cancelled.")

            else:
                print("❌ Invalid email or password. Please try again.")

        elif choice == "3":
            print("Goodbye!")
            break  

        else:
            print("❌ Invalid option! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()