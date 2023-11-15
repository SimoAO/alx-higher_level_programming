#!/usr/bin/node
exports.esrever = function (list) {
  const ver = [];
  for (let i = 0; i < list.length; i++) {
    ver.unshift(list[i]);
  }
  return ver;
};
