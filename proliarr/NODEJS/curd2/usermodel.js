const mongoose = require('mongoose')


const User_Data = new mongoose.Schema({
    id: {
        type: Number
    },
    Firstname: {
        type: String
    },
    Lastname: {
        type: String
    },
    Email: {
        type: String
    },
    Username: {
        type: String
    },
    Password: {
        type: String
    },
    MobileNumber: {
        type: String
    },
    DeviceToken: {
        type: String
    }

},
{
    versionKey: false,
    collection: 'user_datas'
})


module.exports = mongoose.model('user_datas',User_Data)