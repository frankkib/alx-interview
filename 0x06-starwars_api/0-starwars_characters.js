#!/usr/bin/env node

const axios = require('axios');

async function getMovieCharacters (movieId) {
  const baseUrl = `https://swapi.dev/api/films/${movieId}/`;

  try {
    // Fetch movie details
    const response = await axios.get(baseUrl);
    const movieData = response.data;

    // Get character URLs
    const charactersUrls = movieData.characters;

    // Fetch and print each character's name
    for (const characterUrl of charactersUrls) {
      try {
        const characterResponse = await axios.get(characterUrl);
        console.log(characterResponse.data.name);
      } catch (error) {
        console.error(`Error fetching character data: ${error.message}`);
      }
    }
  } catch (error) {
    console.error(`Error fetching movie data: ${error.message}`);
  }
}

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node script.js <movie_id>');
} else {
  getMovieCharacters(movieId);
}
