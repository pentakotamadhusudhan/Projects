var fs = require('fs');
var http = require('http')

http.createServer((req,res)=>{
    console.log('server is running...')
    fs.appendFile('sample.txt','appended data and here ',function(err){
        if (!err,res)
            res.write('file is running')
            res.end()
            console.log('error occur at append')
    })
}).listen(8080)