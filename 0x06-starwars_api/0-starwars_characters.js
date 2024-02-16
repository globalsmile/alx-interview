#!/usr/bin/node

const request = require('request')
const movieId = process.argv[2]
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`

request(url, async function (error, _response, body) {
  if (error) {
    console.log(error)
  } else {
    const characters = JSON.parse(body).characters
    for (const character of characters) {
      const name = await new Promise((resolve, reject) => {
        request(character, function (error, _response, body) {
          if (error) {
            reject(error)
          } else {
            resolve(JSON.parse(body).name)
          }
        })
      })
      console.log(name)
    }
  }
})
