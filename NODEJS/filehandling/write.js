var fs = require('fs');
var http = require('http')

http.createServer((req,res)=>
{
    fs.writeFile('sample.txt','content write here auto added to sample file',(err)=>{
        if (!err) throw err;
            console.log('Replaced')
    })
    fs.readFile('sample.txt',(err,data)=>{

   
        res.writeHead(200,{'content-type':'text/html'});
        res.write(data)
        res.end()
})
}).listen(8080)