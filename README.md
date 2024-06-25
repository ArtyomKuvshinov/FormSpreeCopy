# FormFun

FormFun is a simple Django application that allows users to create forms and receive submissions via email. It is inspired by Formspree and provides similar functionality for handling form submissions.

## Features

- User registration, login, and logout
- Create forms with unique form IDs
- Display user-specific forms
- Send form submission data to the user's email

## Requirements

- Python 3.6+
- Django 3.0+
- A Gmail account (or any SMTP email service) for sending emails

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ArtyomKuvshinov/FormSpreeCopy.git
    cd FormSpreeCopy
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:

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

7. Open your web browser and go to `http://127.0.0.1:8000/`.

## Email Configuration

To enable email functionality, you need to configure the email settings in `formfun/settings.py`. Add the following settings:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
```
Make sure to set the EMAIL_HOST_USER and EMAIL_HOST_PASSWORD environment variables with your email credentials:
