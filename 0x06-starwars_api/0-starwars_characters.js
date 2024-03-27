#!/usr/bin/node
const request = require('request');

// Function to fetch characters for a given movie ID
function getCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Status:', response.statusCode);
      return;
    }

    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    // Print each character name
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Status:', response.statusCode);
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  });
}

const movieId = process.argv[2];
getCharacters(movieId);
