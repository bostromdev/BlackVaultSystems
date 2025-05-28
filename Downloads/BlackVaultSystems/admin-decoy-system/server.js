const express = require('express');
const app = express();
const port = 3000;

app.use(express.static(__dirname + '/public'));
app.get('/api/status', (req, res) => {
  res.json({ status: 'operational', modules: 3 });
});

app.listen(port, () => {
  console.log(`Admin Decoy System running at http://localhost:${port}`);
});