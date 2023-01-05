var http = require('http');
console.log('server running...')


const cars = ["BMW", "Volvo", "Saab", "Ford", "Fiat", "Audi"];
const v = ''
http.createServer((req,res)=>{
    for (let i=0; i<4; i++){
        m=cars[i];
        console.log(m)
        res.write(m)
        res.end()
    }

}).listen(8080)

