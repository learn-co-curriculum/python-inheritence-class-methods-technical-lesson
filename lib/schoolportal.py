# lib/schoolportal.py

class User:
    """
    Base class for all portal users.
    Shared, class-level state lives here (e.g., all_names).
    """
    all_names = []  # Class attribute to track all user names

    def __init__(self, first_name, last_name, email):
        # Instance attributes (unique per object)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def send_email(self, message):
        """Instance method: behaves on one specific user."""
        return f"Sending email to {self.email}: {message}"

    # ---- Class methods operate on the class, not a single instance ----
    @classmethod
    def add_name_to_all(cls, name):
        """Add a name to the shared class list."""
        cls.all_names.append(name)

    @classmethod
    def user_exists(cls, name):
        """Return True if the name is present in the shared class list."""
        return name in cls.all_names

    def __repr__(self):
        # Helpful for debugging / printouts during the lesson
        return f"{self.__class__.__name__}({self.first_name!r}, {self.last_name!r}, {self.email!r})"


class Teacher(User):
    """Teacher subclass extends User with knowledge domain."""
    def __init__(self, first_name, last_name, email, knowledge):
        # Reuse User's initializer for shared attrs
        super().__init__(first_name, last_name, email)
        self.knowledge = knowledge

    def teach(self):
        return f"{self.first_name} is teaching {self.knowledge}."


class Student(User):
    """Student subclass extends User with GPA."""
    def __init__(self, first_name, last_name, email, gpa):
        super().__init__(first_name, last_name, email)
        self.gpa = gpa

    def learn(self):
        return f"{self.first_name} is learning. Current GPA: {self.gpa}."


# ---- Example usage (optional for the lesson; useful during development) ----
if __name__ == "__main__":
    # Create users
    teacher1 = Teacher("Alice", "Johnson", "alice@school.com", "Math")
    student1 = Student("Bob", "Miller", "bob@school.com", 3.8)

    # Add names to the shared class list
    User.add_name_to_all(teacher1.first_name)
    User.add_name_to_all(student1.first_name)

    print(User.all_names)              # ['Alice', 'Bob']
    print(User.user_exists("Alice"))   # True
    print(teacher1.teach())            # Alice is teaching Math.
    print(student1.learn())            # Bob is learning. Current GPA: 3.8.