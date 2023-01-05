const mongoose = require('mongoose');
const auto = require('mongoose-auto-increment');

const brandname = mongoose.Schema({
    id : {type:Number},
    password:{type:String},
    name:{type: String},
    Date : {type: Date,default: Date.now}
},{
    collection: 'mycollection'
});




module.exports = mongoose.model('Brandname',brandname)