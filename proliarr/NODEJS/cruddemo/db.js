const mongoose = require('mongoose') // import mongoose

mongoose.connect('mongodb://127.0.0.1:27017/CrudDB',(err) =>{
    if (!err)  
        console.log('mongodb is connected succesfully' );
    else
        console.log('connection falied in mongodb' + JSON.stringify(err,undefined,2));
});

module.exports = mongoose;
