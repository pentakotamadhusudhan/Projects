const  express= require('express');
const app = express();
const BrandName = require('./model')

app.put('/:id', async(req, res) => {
    try {  
      const up =   await BrandName.findOneAndUpdate(req.params.id)
      res.json(up)
    }catch(err) {
        console.log(err.message)
    }
})
module.exports = app