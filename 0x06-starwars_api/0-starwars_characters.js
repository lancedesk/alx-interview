#!/usr/bin/node
/**
 * Fetch Starwars Characters
 */
const request = require('request');

function getCharacter (urls)
{
  if (urls.length === 0)
  {
      return;
  }
  request.get(urls[0], (_error, _response, body) =>
  {
    console.log(JSON.parse(body).name);
    getCharacter(urls.slice(1));
  });
}

request.get(
  'https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
  (_error, _response, body) =>
  {
    const characters = JSON.parse(body).characters;
    getCharacter(characters);
  }
);
