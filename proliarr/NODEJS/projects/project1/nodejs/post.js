const  express= require('express');
const BrandName = require('./model')
const app = express();
const bodyparser = require('body-parser'); 

const bcrypt = require('bcrypt')

app.post('/', async(req, res)=>{
    
    const {id}= req.body;
    const {name} = req.body;
    const {password} = req.body;
    // const salt = await bcrypt.genSalt()
    // const hashpassword = await bcrypt.hash(password, salt)
    try {
        const newData =  BrandName({id,name,password});
    
        await newData.save();
        return res.json(await BrandName.find());
     }
     catch (err) {
        console.log(err);
     }
})
module.exports = app