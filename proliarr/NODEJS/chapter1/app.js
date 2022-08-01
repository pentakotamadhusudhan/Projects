var http = require('http');
var dt= require('./datetime'); //our indivual module


http.createServer((req,res)=>{
    const lis=['1','2','3','5','3','4']
    console.log(lis)
    res.write(lis)
    res.end()
}).listen(8080)