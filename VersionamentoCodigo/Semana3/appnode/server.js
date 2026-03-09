const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const mysql = require('mysql2');

const app = express();
const port = process.env.PORT || 3000;

// configure body parser
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

// mysql connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'joao',
  password: '12345678',
  database: 'appnode'
});

db.connect(err => {
  if (err) {
    console.error('MySQL connection error:', err);
    process.exit(1);
  }
  console.log('Connected to MySQL');
});

// route to serve registration form
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// handle form submission
app.post('/register', (req, res) => {
  const { name, address, phone, city } = req.body;
  const sql = 'INSERT INTO users (name, address, phone, city) VALUES (?, ?, ?, ?)';
  db.execute(sql, [name, address, phone, city], (err, results) => {
    if (err) {
      console.error('Insert error:', err);
      return res.status(500).send('Database error');
    }
    res.send('Registration successful');
  });
});

// route to list all users
app.get('/users', (req, res) => {
  const sql = 'SELECT * FROM users';
  db.execute(sql, (err, results) => {
    if (err) {
      console.error('Query error:', err);
      return res.status(500).send('Database error');
    }
    let html = '<h1>Lista de Usuários</h1><ul>';
    results.forEach(user => {
      html += `<li>${user.name} - ${user.address} - ${user.phone} - ${user.city}</li>`;
    });
    html += '</ul><a href="/">Voltar ao Cadastro</a>';
    res.send(html);
  });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
