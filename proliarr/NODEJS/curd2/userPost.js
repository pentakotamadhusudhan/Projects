const express = require('express')
const app = express()
const User_Data = require('./usermodel')
const checkAuth = require('./jwt_token')
const bodypaeser = require('body-parser')

// app.use(express.json());
app.post('/', checkAuth,  async(req, res)=>{
   //  const {id} = req.params;
   //  console.log(id);
   //  const {Firstname} = req.body;
   //  const {Lastname} = req.body;
   //  const {Email} = req.body;
   //  const {Username} = req.body;
   //  const {Password} = req.body;
   //  const {MobileNumber} = req.body;
   //  const {DeviceToken} = "reqbody";
    try {
        const newData =  User_Data({id:req.body.id,Firstname:req.body.Firstname,Lastname:req.body.Lastname,Email:req.body.Email,Username:req.body.Username,Password:req.body.Password,MobileNumber:req.body.MobileNumber,DeviceToken:req.body.DeviceToken});
        await newData.save();
        return res.json(newData);
     }
     catch (err) {
        console.log(err);
     }
})

// app.post('/', async(req, res) => {
//     const userdata = new User_Data({
//         Firstname: req.body,
//         Lastname: req.body,
//         Email: req.body,
//         Username: req.body,
//         Password: req.body,
//         MobileNumber: req.body,
//         DeviceToken:req.body
//     })
//     try{
//         // console.log(userdata)
//         const a1 = await userdata.save()
//         console.log("aa")
//         return res.json(a1)
//     }
//     catch(err){
//         res.send(err)
//     }
// })

module.exports = app