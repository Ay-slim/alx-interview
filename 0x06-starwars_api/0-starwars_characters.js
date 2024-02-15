#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, async function (error, _, body) {
  if (error) {
    console.log(error);
  } else {
    const chars = JSON.parse(body).characters;
    for (const char of chars) {
      const res = await new Promise((resolve, reject) => {
        request(char, (error, _, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      console.log(res);
    }
  }
});
