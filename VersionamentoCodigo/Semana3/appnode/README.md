# appnode

Simple Node.js application with a registration page that stores user information in a MySQL database.

## Setup

1. Install dependencies:
   ```bash
   cd /home/joao/workspace/appnode
   npm install
   ```

2. Create the MySQL database and table:
   ```sql
   CREATE DATABASE IF NOT EXISTS appnode;
   USE appnode;

   CREATE TABLE IF NOT EXISTS users (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(255) NOT NULL,
     address VARCHAR(255) NOT NULL,
     phone VARCHAR(50) NOT NULL,
     city VARCHAR(100) NOT NULL,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

   Adjust user/password in `server.js` if necessary.

3. Start the server:
   ```bash
   npm start
   ```

4. Open a browser at [http://localhost:3000](http://localhost:3000) to view the registration form.


## Endpoint

- `GET /` - serves the form
- `POST /register` - handles form submission and inserts into `users` table
- `GET /users` - lists all registered users
- `POST /register` - handles form submission and inserts into `users` table

