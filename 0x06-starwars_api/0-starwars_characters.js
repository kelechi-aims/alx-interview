#!/usr/bin/node

// Import the 'util' module for promise-based functionality
const util = require('util');

// Import the 'request' module and promisify it to allow for async/await syntax
const request = util.promisify(require('request'));

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// Async function to fetch and display characters from a Star Wars movie
async function fetchMovieCharacters (movieId) {
  // Construct the URL for fetching movie details based on the movie ID
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  try {
    // Make a GET request to fetch movie details
    const response = await (await request(movieUrl));

    // Parse the JSON response body into an object
    const movieData = JSON.parse(response.body);

    // Extract the characters associated with the movie
    const characters = movieData.characters;

    // Iterate through each character URL and fetch character details
    for (const characterUrl of characters) {
      const characterResponse = await (await request(characterUrl));
      const characterData = JSON.parse(characterResponse.body);
      console.log(characterData.name);
    }
  } catch (error) {
    // Handle any errors that occur during the process
    console.error('Error:', error.message);
  }
}

// Call the fetchMovieCharacters function with the provided movie ID
fetchMovieCharacters(movieId);
