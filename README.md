# Flask Blog API with Payment and Subscription Integration

This project is a REST API built with Flask that powers a blog site, including functionalities for managing users, profiles, blog posts, videos, and administrative features. The API also integrates payment and subscription methods using Stripe.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Migrations](#database-migrations)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Payment and Subscription Integration](#payment-and-subscription-integration)
- [Deployment](#deployment)
- [License](#license)

## Features

- **User Management:** Create, update, and manage users and profiles.
- **Blog Management:** Create, update, and delete blog posts.
- **Video Management:** Upload, manage, and display videos.
- **Admin Features:** Manage site content, send mass emails, and view subscription status.
- **Payment Integration:** Handle payments and subscriptions via Stripe.
- **JWT Authentication:** Secure API endpoints with JSON Web Tokens (JWT).
- **SQLite Database:** Manage data using SQLite, with support for migrations.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Environment Variables:**
   Create a `.env` file or export the necessary environment variables:
   ```bash
   export SECRET_KEY='your-secret-key'
   export JWT_SECRET_KEY='your-jwt-secret-key'
   export STRIPE_API_KEY='your-stripe-api-key'
   export MAIL_USERNAME='your-email@example.com'
   export MAIL_PASSWORD='your-email-password'
   ```

2. **Configuration File:**
   The `config.py` file includes all necessary configurations for the project, including database URI, JWT settings, and email server details.

## Database Migrations

1. **Initialize the Database:**
   ```bash
   flask db init
   ```

2. **Create and Apply Migrations:**
   ```bash
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

## Running the Application

1. **Run the Flask Application:**
   ```bash
   flask run
   ```

2. **Access the API:**
   Open your browser or API client (like Postman) and navigate to `http://127.0.0.1:5000/`.

## API Endpoints

Here are some of the key endpoints available in this API:

- **User Management:**
  - `POST /users`: Create a new user
  - `GET /users/<id>`: Get user details

- **Blog Management:**
  - `POST /blogs`: Create a new blog post
  - `GET /blogs/<id>`: Get blog post details

- **Video Management:**
  - `POST /videos`: Upload a new video
  - `GET /videos/<id>`: Get video details

- **Admin Management:**
  - `POST /admin/send-emails`: Send mass emails
  - `GET /admin/subscriptions`: View all subscriptions

- **Payment and Subscription:**
  - `POST /create-checkout-session`: Create a Stripe checkout session
  - `POST /webhook`: Stripe webhook for managing subscription events

## Payment and Subscription Integration

This API integrates with Stripe to handle payments and subscriptions. The `create-checkout-session` endpoint allows clients to initiate a payment, and the `webhook` endpoint processes events such as successful payments or subscription renewals.

### Testing Payments

Use the test keys provided by Stripe during development to simulate payments without real transactions.

## Deployment

To deploy this API:

1. **Upload to cPanel:**
   - Compress your project folder and upload it to your cPanel file manager.
   - Extract the files and configure your Python application in cPanel.

2. **Set Environment Variables:**
   - Use cPanel’s environment management tool to set your environment variables.

3. **Run the Application:**
   - Start your Flask application through the cPanel interface.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
