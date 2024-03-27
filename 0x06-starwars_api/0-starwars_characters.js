#!/usr/bin/node
const request = require('request');
const process = require('process');

function getMovieCharacters (movieId) {
  return new Promise((resolve, reject) => {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
    request.get(url, (error, response, body) => {
      if (error) {
        reject(new Error(error));
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch movie data for movie ID ${movieId}`));
      } else {
        const movieData = JSON.parse(body);
        const charactersUrls = movieData.characters;
        const charactersNames = [];
        let charactersCount = 0;
        charactersUrls.forEach(characterUrl => {
          request.get(characterUrl, (error, response, body) => {
            if (!error && response.statusCode === 200) {
              const characterData = JSON.parse(body);
              charactersNames.push(characterData.name);
              charactersCount++;
              if (charactersCount === charactersUrls.length) {
                resolve(charactersNames);
              }
            } else {
              reject(new Error(`Failed to fetch character data for ${characterUrl}`));
            }
          });
        });
      }
    });
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId)
  .then(characters => {
    characters.forEach(character => {
      console.log(character);
    });
  })
  .catch(error => {
    console.error(error);
  });
