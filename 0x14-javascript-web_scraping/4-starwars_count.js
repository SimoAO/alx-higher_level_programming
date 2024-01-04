#!/usr/bin/node
const request = require('request');
const rURL = process.argv[2];
let count = 0;
const id = 18;

request(rURL, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const jbr = JSON.parse(body).results;
    const nf = JSON.parse(body).count;
    for (let i = 0; i < nf; i++) {
      const ll = jbr[i].characters;
      for (let j = 0; j < ll.length; j++) {
        const chId = parseInt(ll[j].split('/').slice(-2, -1)[0]);
        if (chId === id) {
          count += 1;
          break;
        }
      }
    }
    console.log(count);
  }
});
