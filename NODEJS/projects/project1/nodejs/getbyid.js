const  express= require('express');
const app = express();
const BrandName = require('./model')



app.get('/:id', async(req, res)=>{
    try{

        const Data = await BrandName.findOne({id:req.params.id})
        if(Data==null){
            res.status(404).send({message: 'No such data is not exisit '})
        }
        else{
            res.json(Data)
        console.log(Data.name)
        }
        
        
    }
    catch(err){
        console.log(err.message)}
})



module.exports = app