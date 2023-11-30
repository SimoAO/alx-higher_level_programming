#!/usr/bin/node
if (parseInt(process.argv[3])) {
  console.log(process.argv.slice(2).sort((a, b) => b - a)[1]);
} else {
  console.log('0');
}
