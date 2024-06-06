#!/usr/bin/node
/**
 * Fetch Starwars Characters
 */
const req = require('request');

const movieId = process.argv[2];
const movieLink = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

req(movieLink, (err, res, body) => {
  if (err) console.log(err);
  const i = 0;
  const characters = JSON.parse(body).characters;
  movieChar(characters, i);
});

const movieChar = function (url, i) {
  req(url[i], (err, res, body) => {
    if (err) console.log(err);
    console.log(JSON.parse(body).name);
    if (++i < url.length) {
      movieChar(url, i++);
    }
  });
};
