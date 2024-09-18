# Library Management System

This project consists of two independent API services to manage a library's collection of books. The APIs enable users to browse books and borrow them, while providing administrators the ability to manage the book catalogue and monitor library users.

## Project Structure

- **Frontend API**: Allows library users to enroll, browse books, filter by category or publisher, and borrow books.
- **Backend/Admin API**: Allows library administrators to add or remove books, manage users, and view unavailable books.

Both services use separate data stores and communicate changes (like adding new books) between the APIs. The services are containerized using Docker for ease of deployment.

## Features

### Frontend API

The Frontend API provides the following endpoints for users:

1. **Enroll Users**

   - Endpoint: `POST /users/enroll/`
   - Description: Enroll a new user by providing their first name, last name, and email.

2. **List All Available Books**

   - Endpoint: `GET /books/`
   - Description: Retrieve all books currently available for borrowing.

3. **Get Single Book by ID**

   - Endpoint: `GET /books/{book_id}`
   - Description: Get details about a specific book using its ID.

4. **Filter Books**

   - Endpoint: `GET /books/filter/`
   - Description: Filter books by publisher or category (e.g., fiction, technology, science).

5. **Borrow a Book**
   - Endpoint: `POST /books/borrow/{book_id}`
   - Description: Borrow a book by its ID, specifying the number of days to borrow it.

### Backend/Admin API

The Admin API provides the following endpoints for administrators:

1. **Add New Books**

   - Endpoint: `POST /admin/books/add/`
   - Description: Add new books to the library's catalogue.

2. **Remove a Book**

   - Endpoint: `DELETE /admin/books/{book_id}`
   - Description: Remove a book from the catalogue by its ID.

3. **List All Users**

   - Endpoint: `GET /admin/users/`
   - Description: Retrieve a list of all enrolled users.

4. **List Users and Their Borrowed Books**

   - Endpoint: `GET /admin/users/borrowed-books/`
   - Description: Retrieve a list of users and the books they have borrowed.

5. **List Unavailable Books**
   - Endpoint: `GET /admin/books/unavailable/`
   - Description: List all books currently borrowed and unavailable for lending, along with the date they will be available.

## Communication Between Frontend and Backend

When an admin adds a new book via the backend API, the frontend API must be updated to reflect this change. This is achieved through communication between the services, ensuring both databases stay in sync.

## Data Models

### User

- `id` (int): Unique identifier
- `firstname` (string): User's first name
- `lastname` (string): User's last name
- `email` (string): User's email (unique)

### Book

- `id` (int): Unique identifier
- `title` (string): Book title
- `author` (string): Book author
- `publisher` (string): Book publisher
- `category` (string): Book category (e.g., fiction, technology)
- `is_available` (bool): Availability status of the book
- `available_on` (date): When the book will become available again if currently borrowed

### Borrow

- `id` (int): Unique identifier
- `user_id` (int): ID of the user borrowing the book
- `book_id` (int): ID of the borrowed book
- `borrow_date` (date): Date of borrowing
- `return_date` (date): Expected return date

## Database

Each service has its own data store:

- The **frontend API** uses a SQLite database (`library.db`).
- The **backend API** uses a PostgreSQL database (configured in `docker-compose.yml`).

## Deployment

The application is containerized with Docker and can be easily deployed using the provided `docker-compose.yml` file. The setup defines services for both the frontend and backend APIs, along with a PostgreSQL database for the backend.

### Steps to Deploy

1. Ensure Docker and Docker Compose are installed on your system.
2. Clone the repository and navigate to the project directory.
3. Build and start the services:
   ```bash
   docker-compose up --build
   ```
4. The frontend API will be accessible at http://localhost:8000.
5. The backend/admin API will be accessible at http://localhost:8001.

### Testing

Unit and integration tests are provided using pytest. Run the tests with the following command:
`pytest`

### Dependencies

The project dependencies are listed in requirements.txt and include:

- FastAPI
- SQLAlchemy
- Uvicorn
- Pydantic
- Pytest

### License

This project is licensed under the MIT License.
