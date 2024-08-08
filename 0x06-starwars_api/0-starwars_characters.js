#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
    console.log("Please provide a Movie ID as a positional argument.");
    process.exit(1);
}

// Base URL for the Star Wars API
const baseUrl = 'https://swapi-api.alx-tools.com/api/';

// URL to fetch the film information
const filmUrl = `${baseUrl}films/${movieId}/`;

// Fetch film data
request(filmUrl, { json: true }, (error, response, body) => {
    if (error) {
        console.error('Error fetching the movie:', error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error(`Failed to retrieve the movie. Status Code: ${response.statusCode}`);
        return;
    }

    // Fetch the list of character URLs
    const characterUrls = body.characters;

    if (!characterUrls || characterUrls.length === 0) {
        console.log("No characters found for this movie.");
        return;
    }

    // Function to fetch and print each character name
    const fetchCharacter = (url) => {
        return new Promise((resolve, reject) => {
            request(url, { json: true }, (err, res, charBody) => {
                if (err) {
                    reject(err);
                } else if (res.statusCode !== 200) {
                    reject(new Error(`Failed to retrieve character. Status Code: ${res.statusCode}`));
                } else {
                    console.log(charBody.name);
                    resolve();
                }
            });
        });
    };

    // Fetch all characters sequentially
    (async () => {
        for (let characterUrl of characterUrls) {
            try {
                await fetchCharacter(characterUrl);
            } catch (err) {
                console.error('Error fetching character:', err.message);
            }
        }
    })();
});

