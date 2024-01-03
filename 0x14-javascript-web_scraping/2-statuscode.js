#!/usr/bin/node
const request = require('request');
const rURL = process.argv[2];

request(rURL, function (err, resp) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', resp.statusCode);
  }
});
