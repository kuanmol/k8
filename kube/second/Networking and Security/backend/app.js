const express = require('express');
const mongoose = require('mongoose');

const app = express();
const PORT = process.env.APP_PORT || 3000;
const MONGO_URI = process.env.MONGO_URI;

mongoose.connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Failed to connect to MongoDB:', err));

app.get('/', (req, res) => {
    res.send('Backend is running!');
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
