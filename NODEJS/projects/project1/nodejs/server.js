var express = require('express');
const mongoose = require('mongoose')
const db=require('./db.js')
const app = express();
const BrandName = require('./model');
const getcall = require('./get.js');
const postcall = require('./post.js');
const getbyid = require('./getbyid.js');
const update = require('./update.js');
const login = require('./login.js');





app.use(express.json())
app.use('/post',postcall)
app.use('/get', getcall)
app.use('/getid', getbyid)  
app.use('/update',update)
app.use('/login', login)

// app.use(function(req, res, next) {
//   res.header('Access-Control-Allow-Origin', '*');
//   res.header('Access-Control-Allow-Methods','GET, POST, PUT, DELETE');
//   res.header('Access-Control-Allow-Headers','Content-Type');
//   next();
// });


app.listen(8000,function(){
  console.log('app listening port 8000!')
});