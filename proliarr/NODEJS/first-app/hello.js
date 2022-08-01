const http = require('http');
const server = http.createServer((request,response) => {
    response.end('hello world\n');
});
server.listen(8080, () => {
    console.log('server is running.....');
});
