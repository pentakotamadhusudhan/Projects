const express = require('express')
const app = express()
const User_Data = require('./usermodel')
const checkAuth = require('./jwt_token')


app.get('/:id', async(req, res) => {
    try{

            const user = await User_Data.findOne({id:req.params.id})
            res.json(user)
    }
    catch(err){
        res.send('Error' + err)
    }

})
 
module.exports = app