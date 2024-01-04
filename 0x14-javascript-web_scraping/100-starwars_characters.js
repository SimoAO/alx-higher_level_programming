#!/usr/bin/node
const request = require('request');
const rURL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(rURL, function (err, resp, body) {
  if (err) console.log(err);
  const ch = JSON.parse(body).characters;
  ch.forEach((character) => {
    request(character, function (err, resp, body) {
      if (err) console.log(err);
        console.log(JSON.parse(body).name);
      });
  });
});
