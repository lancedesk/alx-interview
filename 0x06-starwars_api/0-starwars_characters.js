#!/usr/bin/node
const fetch = require('node-fetch');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Check if movieId is provided
if (!movieId) {
    console.error('Usage: ./0-starwars_characters.js <Movie ID>');
    process.exit(1);
}

// API URL for the movie
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

async function fetchCharacters(url) {
    try {
        // Fetch the movie details
        const response = await fetch(url);
        const film = await response.json();

        // Get the list of character URLs
        const characters = film.characters;

        // Fetch and print each character's name sequentially
        for (const characterUrl of characters) {
            const characterResponse = await fetch(characterUrl);
            const character = await characterResponse.json();
            console.log(character.name);
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Call the function to fetch and print characters
fetchCharacters(url);
