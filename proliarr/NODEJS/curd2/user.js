const express = require('express')
const router = express.Router()
const User_Data = require('./usermodel')
const checkAuth = require('./jwt_token')

router.get('/', checkAuth, async(req, res) => {
    // res.send("aaaaa")
    try{
            const userdata = await User_Data.find()
            res.json(userdata)
    }
    catch(err){
        res.send('Error' + err)
    }

})

module.exports = router