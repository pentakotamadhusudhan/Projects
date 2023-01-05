const express = require("express");
const app = express();
const jwt = require('jsonwebtoken');
const token = require('./login')
//console.log(token)
function ensureToken(req, res, next){
    // console.log(token)
    const bearerHeader = req.headers["authorization"];
    console.log(bearerHeader)
    if (typeof bearerHeader !== 'undefined'){
        const bearer = bearerHeader.split(" ");
       // console.log(bearer)
        const bearerToken = bearer[1];
        // console.log(bearerToken)
        req.token = bearerToken;
        next();
    } else {
        res.sendStatus(403);
    }
}

module.exports = ensureToken