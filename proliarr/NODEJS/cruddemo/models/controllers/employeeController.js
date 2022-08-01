const express = require('express');

var router  = express.Router();
var ObjectId = require('mongoose').Types.ObjectId

router.get('/',(req,res) =>{
    Employee.find((err,docs) => {
        if (!err){res.send(docs);}
        else { console.log('error occur in retriving :' + JSON.stringify(err,undefined,2));}
    });
});

router.post('/post',(req,res) =>{
    var emp = new Employee({
        name = req.body,
        position = req.body,
        
    })
    // save is a key word to save all our records 
    emp.save((err,doc) =>{
        if (!err){ res.send(doc);}
        else { console.log('error occured at save/post call ;' +JSON.stringify(err,undefined,2));
    }
    })
})



module.exports = router;