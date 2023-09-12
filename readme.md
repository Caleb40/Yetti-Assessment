
# Yetti Assessment: Django User Authentication

## Description

This Django project demonstrates user authentication features, including user registration, login, and logout. It also includes comprehensive tests for various scenarios, ensuring both functionality and security.

## Setup

Follow these steps to set up and run the project:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/caleb40/Yetti-Assessment.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd Yetti-Assessment
   ```

3. **Install Pipenv (Optional):**

   ```bash
   python -m pip install pipenv
   ```
   
4. **Install the Requirements from Pipfile:**

   ```bash
   pipenv install
   ```

5. **Activate the Virtual Environment:**
     ```bash
    pipenv shell
     ```

6. **Set Up the Database:**

   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser (Optional):**

   You can create an admin superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

9. **Access the Application:**
   - Open your web browser and go to `http://127.0.0.1:8000/` to access the "Hello World" page.
   - Register using the endpoint `http://127.0.0.1:8000/auth/register/`.
   - Login using the endpoint `http://127.0.0.1:8000/auth/login/`.
   - To access the admin panel (if you created a superuser), go to `http://127.0.0.1:8000/admin/`.

## Running Tests

To run the tests for this project, use the following command:

```bash
python manage.py test
```

This command will execute all the tests defined in the project, including unit tests for user registration, login, and logout, as well as security-related tests.
