const express = require("express");
const app = express();
const jwt = require('jsonwebtoken');

app.post('/token', function(req, res){
    const user = {id : 3}
    const token = jwt.sign({user}, 'my_secret_key');
    return res.send({token
    });
});

module.exports = app