# Star Wars API

`0-starwars_characters.js` prints the characters of a Star Wars movie, one
name per line, in the same order as the `characters` list returned by the
`/films/` endpoint of the [Star Wars API](https://swapi-api.hbtn.io/).

The names are fetched one after the other, so the output keeps that order.

## Requirements

- Node 10
- The `request` module: `npm install request --global` and
  `export NODE_PATH=/usr/lib/node_modules`

## Usage

```
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
...
```
