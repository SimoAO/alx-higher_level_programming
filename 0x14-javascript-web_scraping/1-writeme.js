#!/usr/bin/node
const fs = require('fs');
const fp = process.argv[2];
const cont = process.argv[3];
fs.writeFile(fp, cont, 'utf8', (err) {
  if (err) {
    console.log(err);
  }
});
