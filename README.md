# Technical Lesson: Inheritance, Class Attributes, and Class Methods

In this lesson, you will learn how to implement inheritance in Python classes, as well as how to use class attributes and class methods to manage shared data and behavior across instances.

## Scenario

You are working on a school administration system that requires a portal for students and teachers. To facilitate this, you will create a base `User` class and two subclasses, `Teacher` and `Student`. You will also implement class attributes and class methods to track all users and manage user data efficiently.

## Learning Goals

- Understand how to create a parent class and child classes using inheritance.
- Use `super()` to access and extend parent class functionality.
- Define and use class attributes to store data shared across all instances.
- Create class methods to manipulate class-level data.
- Implement instance methods unique to subclasses.

## Tasks

1. Create a `User` superclass with shared attributes and methods.
2. Create `Teacher` and `Student` subclasses that inherit from `User`.
3. Add a class attribute to `User` to track all user names.
4. Implement class methods to add new users and check if a user exists.
5. Add instance methods specific to `Teacher` (`teach`) and `Student` (`learn`).

## Installation

Clone the repository and install dependencies:
- git clone https://github.com/walbeck85/course_5_summative_lab.git
- cd course_5_summative_lab
- Open the project in VS Code.
- Run `pipenv install` to install dependencies.
- Run `pipenv shell` to activate the virtual environment.

## Implementation Overview

- **User class:** Contains first name, last name, and email attributes. Includes a class attribute `all_names` to track all user full names and class methods to add and check users.
- **Teacher class:** Inherits from `User` and includes a knowledge base attribute and a `teach` method that returns a random knowledge string.
- **Student class:** Inherits from `User` and includes a GPA attribute and a `learn` method that appends knowledge strings to the student's knowledge list.

## Additional Resources

- [GitHub Repository](https://github.com/learn-co-curriculum/python-inheritence-class-methods-technical-lesson)

Use this lesson to practice designing clean, maintainable object-oriented code that leverages Python’s inheritance and class features.
