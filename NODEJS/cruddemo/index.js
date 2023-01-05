// ./src/index.js
// importing the dependencies  or plackages
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
// we call  the db.js file below 
const {mongoose } =  require('./db.js');
// call the employeeController file and stored in employeeController

var employeeController = require('./models/controllers/employeeController.js');

var app  = express();
app.use(bodyParser.json());
app.listen(3000, (err) =>{
    if (!err)
        console.log('server is started ar port 3000')
    else
        console.log('server failed')
});
app.use('./emp',employeeController);