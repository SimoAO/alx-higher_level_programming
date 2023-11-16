#!/usr/bin/node
const dict = require('./101-data').dict;
const nD = {};
for (const key in dict) {
  if (!nD[dict[key]]) {
    nD[dict[key]] = [];
  }
  nD[dict[key]].push(key);
}
console.log(nD);
