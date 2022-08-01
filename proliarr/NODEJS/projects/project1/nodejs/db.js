const mongoose = require('mongoose');
const  express= require('express');
const app = express();



mongoose.connect('mongodb://localhost:27017/CrudDB').then(()=>
  console.log('Connected to MongoDB Database port ')
).catch(err => console.log(err))

module.exports = mongoose