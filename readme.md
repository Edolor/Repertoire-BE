
# Portfolio Backend

This repository contains the backend code for my portfolio, built using **Django** and **PostgreSQL**. The project includes APIs for handling various functionalities, and it is designed to run within a Dockerized environment, making it easy to deploy and scale.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
  - [Docker Setup](#docker-setup)
  - [Local Development Setup](#local-development-setup)
  - [Production Setup](#production-setup)
- [Environment Variables](#environment-variables)
- [API Rate Limiting](#api-rate-limiting)
- [Static and Media Files](#static-and-media-files)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Project Overview

This project serves as the backend for my portfolio website. It includes features like contact forms, authentication, project management, and more, powered by **Django** and **Django REST Framework**.

The backend is designed to:
- Serve dynamic content via APIs.
- Handle user authentication and management.
- Store and serve static and media files.
- Integrate with Google Drive for file storage.

### Features
- API Rate Limiting
- Cross-Origin Resource Sharing (CORS) support
- PostgreSQL database integration
- File storage with Google Drive
- Dockerized for easy setup and deployment

## Technologies
- **Django** (Backend Framework)
- **Django REST Framework** (API Framework)
- **PostgreSQL** (Database)
- **Docker** (Containerization)
- **Gunicorn** (WSGI server)
- **Nginx** (Reverse Proxy and SSL)
- **CORS Headers** (Cross-origin support)
- **Whitenoise** (Static File Management)
- **Google Drive API** (File Storage)

## Setup Instructions

### Docker Setup
To get started with Docker, clone the repository and use the provided `docker-compose` files to set up the backend, Nginx, and PostgreSQL services.

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/portfolio-backend.git
   cd portfolio-backend
   ```

2. Build and start the containers:

   ```bash
   docker-compose -f docker-compose.prod.yml up --build
   ```

   This command will:
   - Build the backend container using the production Dockerfile (`Dockerfile.prod`).
   - Set up the PostgreSQL database container.
   - Configure Nginx as a reverse proxy for HTTPS traffic.

3. Once the containers are running, the backend will be available at `https://yourdomain.com` (assuming you have configured SSL).

### Local Development Setup
For local development without Docker, you can set up the backend by following these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/portfolio-backend.git
   cd portfolio-backend
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scriptsctivate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add the necessary environment variables (refer to [Environment Variables](#environment-variables)).

5. Run migrations and start the server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

   Your local backend will now be accessible at `http://127.0.0.1:8000`.

### Production Setup
For production, you'll need to configure Docker and deploy the backend on a server or cloud provider (e.g., AWS EC2).

1. Use `docker-compose.prod.yml` to build and run the containers:

   ```bash
   docker-compose -f docker-compose.prod.yml up --build
   ```

2. Make sure the `.env` file is included, and configure SSL certificates for Nginx.

3. Ensure that the environment variables are set up correctly for production (see [Environment Variables](#environment-variables)).

4. The backend will be accessible over HTTPS, and Nginx will manage the reverse proxy and SSL encryption.

## Environment Variables

The backend relies on the following environment variables that should be added to your `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=true
DATABASE_NAME=your-db-name
DATABASE_PORT=5432
DATABASE_USER=your-db-user
DATABASE_PASSWORD=your-db-password
DATABASE_HOST=localhost
EMAIL_HOST=smtp.gmail.com
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-email-password
EXTERNAL_HOSTNAME=your-external-hostname
```

Make sure to replace the placeholder values with your actual credentials and configurations.

## API Rate Limiting

This project implements API rate limiting for specific endpoints, such as the contact form submission. The rate limit is configured using Django REST Framework's throttle settings.

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'contact-message': '10/day',
    },
}
```

This configuration ensures that users can only send 10 messages per day via the contact form.

## Static and Media Files

### Static Files

Static files (CSS, JavaScript, images) are handled by **Whitenoise** and are served by Nginx in production.

- **STATIC_URL**: `static/`
- **STATIC_ROOT**: `/path/to/staticfiles`

### Media Files

Uploaded media files are stored in the `/media/` directory.

- **MEDIA_URL**: `media/`
- **MEDIA_ROOT**: `/path/to/media`

These files are managed within Docker volumes, ensuring persistence across container restarts.

## Deployment

To deploy the backend using AWS or another cloud provider, follow these steps:

1. Set up a cloud server (e.g., EC2).
2. SSH into the server and clone the repository.
3. Install Docker and Docker Compose.
4. Set up environment variables and SSL certificates.
5. Run the application using `docker-compose.prod.yml` as described in [Production Setup](#production-setup).

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.