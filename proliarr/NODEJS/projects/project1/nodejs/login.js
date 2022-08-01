const  express= require('express');
const app = express();
const BrandName = require('./model')
const bcrypt = require('bcrypt')
const getcall = require('./get.js');

app.post('/',async(req, res)=>{
    // res.sendFile('login.html',{root : __dirname})
    const { name } = req.body
    const { password } = req.body
     
    // const salt = await bcrypt.genSaltSync()
    // hashpassword = bcrypt.hashSync(password, salt)
    const user = await BrandName.findOne({name:name})
    console.log(user.name)
    console.log(user.password)
    if (user.password == password){
       
        console.log('username and name are  same')
        res.send({success: true,user})
        
    }// console.log(user.password)
    // try{
    //     if(await bcrypt.compare(password,user.password)){
    //         res.sendFile('index.html',{root:__dirname})
    //         console.log('password also matched')
    //     }else{
    //         res.send('else got errror')``
    //     }
    // }catch(e){
    //     return res.status(500).send()
    // }
    
   
});


module.exports = app