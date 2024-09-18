#!/usr/bin/node

const request = require('request');

function getMovieCharacters (movieId) {
  const baseUrl = `https://swapi.dev/api/films/${movieId}/`;

  // Fetch movie details
  request(baseUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error(`Error fetching movie data: ${error.message}`);
      return;
    }

    // Get character URLs
    const charactersUrls = body.characters;

    // Fetch and print each character's name
    charactersUrls.forEach((characterUrl) => {
      request(characterUrl, { json: true }, (error, response, body) => {
        if (error) {
          console.error(`Error fetching character data: ${error.message}`);
          return;
        }
        console.log(body.name);
      });
    });
  });
}

// Get the movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node script.js <movie_id>');
} else {
  getMovieCharacters(movieId);
}
