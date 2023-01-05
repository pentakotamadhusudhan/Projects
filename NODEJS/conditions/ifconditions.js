var http = require('http');
console.log('server running...')
http.createServer((req,res)=>{
    m = 0
    if (m>100){
        res.write('m is less than 10')
        res.end()
    console.log('if is done')       
    }
    else if (m<10){
        res.write('m is less than 10')
        res.end()
    console.log('if else is done')
    }
    else {
        res.write('m is greater than 10')
        res.end()
        console.log('enter to else')
    }
}).listen(8080)