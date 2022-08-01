const express = require('express')
const router = express.Router()
const User_Data = require('./usermodel')
const checkAuth = require('./jwt_token')


router.put('/:id', async(req, res) => {
    try{
        const user = await User_Data.findOne({id:req.params.id})
        console.log(user)
        user.Firstname = req.body.Firstname;
        user.Lastname = req.body.Lastname;
        user.Email = req.body.Email; 
        user.Username = req.body.Username;
        user.Password = req.body.Password;
        user.MobileNumber = req.body.MobileNumber;
        user.DeviceToken = req.body.DeviceToken;
        await user.save()
        res.json(user)
    }
    catch(err){
        res.send('Error' + err)
    }

})
 
module.exports = router