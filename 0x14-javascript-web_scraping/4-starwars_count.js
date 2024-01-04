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
    for (let i = 0; i < jbr.length; i++) {
      const ch = jbr[i].characters;
      for (let j = 0; j < ch.length; j++) {
        const chId = ch[j].split('/').slice(-2, -1)[0];
        if (parseInt(chId) === id) {
          count += 1;
          break;
        }
      }
    }
    console.log(count);
  }
});
