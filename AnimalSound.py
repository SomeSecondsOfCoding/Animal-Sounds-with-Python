#This is an one-file Project for learning purpose:

class Animal:
    def __init__(self, name):  # Constructor Method (fixed incorrect method name)
        self.name = name  # Assigns a name to the object

    def speak(self):  # Method that returns a generic message
        return "I make a sound!"


class Dog(Animal):
    def speak(self):
        return "Woof!"  # Dog says "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


class Bird(Animal):
    def speak(self):
        return "Kuhu!"


# Creating a list (array) of animals
animals = [Dog("Buddy"), Cat("Sherlock"), Cow("Ben"), Bird("Mr. Krick"), Animal("Unknown")]


# Menu flow:
def show_menu():
    print("\n🐾 Animal Sound Menu 🐾")
    print("Choose an animal to see aka hear its sound:")
    for i, animal in enumerate(animals):
        print(f"{i + 1}. {animal.name}")
    print("0. Exit")


def main():
    while True:
        show_menu()  # Fixed: added parentheses to call the function
        choice = input("Enter the number of your choice: ") # Take the Input return a String

        if choice == "0":
            print("Goodbye! 🐾")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(animals):  # Fixed condition logic
            selected_animal = animals[int(choice) - 1]
            print(f"{selected_animal.name} says: {selected_animal.speak()}")
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":  
    main()
