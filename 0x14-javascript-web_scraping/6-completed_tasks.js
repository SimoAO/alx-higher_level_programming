#!/usr/bin/node
const request = require('request');
const rURL = process.argv[2];

request(rURL, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const users = {};
    body.forEach((ToDo) => {
      if (ToDo.completed) {
        if (users[ToDo.userId] === true) {
          users[ToDo.userId] += 1;
        } else {
          users[ToDo.userId] = 1;
        }
      }
    });
    console.log(users);
  }
});
