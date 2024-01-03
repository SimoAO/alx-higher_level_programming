#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const rURL = process.argv[2];
const fp = process.argv[3];

request(rURL, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fp, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
