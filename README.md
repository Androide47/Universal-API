# Blog API with Payment Integration

This is a Flask-based REST API for a blog site, designed to handle user management, profiles, blog posts, video content, and admin functionalities. The API also integrates payment and subscription management using Stripe and PayPal.

## Features

- **User Management:** Sign up, log in, and profile management.
- **Blog Management:** Create, update, delete, and retrieve blog posts.
- **Video Management:** Upload, manage, and retrieve video content.
- **Admin Site:** Manage users, send mass emails, and edit blog and video content.
- **Payment Integration:** Support for Stripe and PayPal for handling payments and subscriptions.
- **SQLite Database:** Used for storing all application data.

## Getting Started

### Prerequisites

- Python 3.7+
- Flask
- SQLite
- Stripe account
- PayPal Developer account

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Androide47/AvanzaStudio.git
   cd AvanzaStudio
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and add the following:

   ```bash
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key
   STRIPE_API_KEY=your-stripe-api-key
   STRIPE_WEBHOOK_SECRET=your-stripe-webhook-secret
   PAYPAL_CLIENT_ID=your-paypal-client-id
   PAYPAL_CLIENT_SECRET=your-paypal-client-secret
   PAYPAL_MODE=sandbox  # 'live' for production
   ```

5. **Run the application:**

   ```bash
   flask run
   ```

### Database Setup

1. **Initialize the SQLite database:**

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

### API Endpoints

#### User Management

- **`POST /api/register`**
  - Register a new user.
- **`POST /api/login`**
  - Log in a user.

#### Blog Management

- **`GET /api/blogs`**
  - Retrieve all blog posts.
- **`POST /api/blogs`**
  - Create a new blog post.
- **`PUT /api/blogs/<id>`**
  - Update an existing blog post.
- **`DELETE /api/blogs/<id>`**
  - Delete a blog post.

#### Video Management

- **`POST /api/videos`**
  - Upload a new video.
- **`GET /api/videos`**
  - Retrieve all videos.
- **`DELETE /api/videos/<id>`**
  - Delete a video.

#### Admin Site

- **`POST /api/admin/send-emails`**
  - Send mass emails to users.
- **`PUT /api/admin/blogs/<id>`**
  - Edit a blog post.
- **`PUT /api/admin/videos/<id>`**
  - Manage video content.

### Payment and Subscription Integration

This API supports both Stripe and PayPal for handling payments and subscriptions.

#### Stripe

- **Endpoint:** `POST /api/stripe/checkout`
- **Description:** Creates a Stripe checkout session for subscription payments.

- **Endpoint:** `POST /api/stripe/webhook`
- **Description:** Handles Stripe webhook events.

#### PayPal

- **Endpoint:** `POST /api/paypal/payment`
- **Description:** Initiates a PayPal payment and redirects the user to PayPal for approval.

- **Endpoint:** `GET /api/paypal/payment/execute`
- **Description:** Executes the PayPal payment after user approval.

- **Endpoint:** `GET /api/paypal/payment/cancel`
- **Description:** Handles payment cancellation.

### Testing

To run the tests, use the following command:

```bash
flask test
```

### Deployment

For deployment, make sure to:

- Set `FLASK_ENV=production`.
- Use `gunicorn` or another WSGI server to serve the app.
- Secure environment variables and keys.

### Contributing

Please feel free to submit issues or pull requests.

### License

This project is licensed under the MIT License.
