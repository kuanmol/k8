const express = require('express');
const app = express();

app.use(express.json());

app.get('/api', (req, res) => {
  res.json({ message: 'Hello from Backend!' });
});

app.listen(3000, () => {
  console.log('Backend running on port 3000');
});
