const { default: mongoose } = require("mongoose")


var Employee = mongoose.model('Employee',{
    name : {type:String},
    postion : {type:String},
    

})

module.exports = { Employee };