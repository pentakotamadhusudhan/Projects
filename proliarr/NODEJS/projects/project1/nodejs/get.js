const  express= require('express');
const app = express();
const BrandName = require('./model')
const list = []
// app.get('/', async(req, res)=>{
//     try{
//         res.sendFile('index.html',{root:__dirname});
//     res.json(await BrandName.where())
//     }
//     catch (err) {
//         console.log(err);}
// })


app.get('/',(req, res) =>{
    BrandName.find((err,docs) =>{
        const x = docs
        const array1 = docs;
        if (!err) {
            res.send(x)
        }
        else {
            console.log("error messsage: " + JSON.stringify(err,undefined,2));
        }
    })

})

module.exports = app