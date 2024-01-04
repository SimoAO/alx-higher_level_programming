#!/usr/bin/node
const request = require('request');
const rURL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(rURL, function (err, resp, body) {
  if (err) console.log(err);
  const ch = JSON.parse(body).characters;
  printCh(ch, 0);
});

function printCh (ch, x) {
  request(ch[x], function (err, resp, body) {
    if (err) console.log(err);
    console.log(JSON.parse(body).name);
    if (x < ch.length - 1) {
      printCh(ch, x + 1);
    }
  });
}
