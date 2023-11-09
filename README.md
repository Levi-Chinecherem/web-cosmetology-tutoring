# Web-Based Cosmetology Tutoring System

## Introduction

The Web-Based Cosmetology Tutoring System is a Django-based web application designed to facilitate cosmetology education through tutorials, quizzes, and progress tracking.

![Screenshot 2](screenshots/screenshot2.png)

## Features

- **Tutorials:** Create, update, and delete tutorials with details such as title, image, category, and description.
- **Steps:** Break down tutorials into steps, each with its content. Order steps to guide users through the tutorial.
- **Categories:** Organize tutorials into categories with names and descriptions.
- **Quizzes:** Create quizzes with questions and multiple-choice answers. Track student progress and scores.
- **User Roles:** Differentiate between instructors and students with custom user roles and permissions.
- **Progress Tracking:** Monitor student progress through quizzes and tutorials.
- **Responsive Design:** The application is designed to work seamlessly on various devices.

## Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi-Chinecherem/web-cosmetology-tutoring.git

   ```
2. Navigate to the project directory:

   ```bash
   cd web-cosmetology-tutoring
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```
5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:

   ```bash
   python manage.py runserver
   ```
7. Access the admin interface at http://localhost:8000/admin/ and log in with the superuser credentials.

### Usage

1. **Tutorials:**

   - Create tutorials via the admin interface.
   - Add steps to tutorials to create a learning path.
2. **Quizzes:**

   - Create quizzes and questions in the admin interface.
   - Assign quizzes to tutorials.
3. **Categories:**

   - Create and manage tutorial categories.
4. **User Roles:**

   - Assign user roles in the admin interface.
5. **Progress Tracking:**

   - Track student progress through the admin interface.

## Screenshots

![Screenshot 1](screenshots/screenshot1.png)
*Caption for Screenshot 1*

![Screenshot 2](screenshots/screenshot2.png)
*Caption for Screenshot 2*

## Sample Output

### Creating a Tutorial

1. Access the admin interface and navigate to Tutorials.
2. Click "Add Tutorial."
3. Fill in the required fields, such as title, image, category, and description.
4. Add steps to the tutorial.
5. Save the tutorial.

### Taking a Quiz

1. Log in as a student.
2. Access the list of available quizzes.
3. Start a quiz and answer the questions.
4. Submit the quiz.

## Contributing

If you would like to contribute to the project, please follow our [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
