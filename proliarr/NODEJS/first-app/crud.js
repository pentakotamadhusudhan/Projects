const {MongoClient} = require('mongodb');
var http = require('http');

http.createServer(function(req, res){
    async function main(){
        const uri = 'mongodb://localhost:27017';
        const client= new MongoClient(uri);
        try{
            await client.connect();
            await createMultilisting(client, [
            {
                Name : "Janapareddy ",
                Bike : "scooty",
                speed : "140km",
                Keys : "Forgot"

            },
            {
                Name : "Rakesh",
                Bike : "scooty",
                speed : "140km",
                Keys : "Forgot"
            },
            {
                Name : "john",
                Bike : "scooty",
                speed : "140km",
                Keys : "Forgot"
            }]
            );
            await createGetListing(client, "Rakesh");
        } catch (e) {
            console.error(e);
        } finally {
            await client.close();
        }
    }

    main().catch(console.error);
    //inserted many datas in mongodb
    async function createMultilisting(client, newlisting){
        const result = await client.db("mobile").collection("ListingsAndReviews").insertMany(newlisting);
        console.log(result.insertedIds);
        console.log(`${result.insertedCount}`);
    }
    //insert one data in mongodb
    async function createlisting(client, newlisting){
        const result = await client.db("mobile").collection("ListingsAndReviews").insertOne(newlisting);
        console.log(`new listing created with the following id: ${result.insertedId}`)
    }
    async function createGetListing(client, nameoflisting){
        const result = await client.db("mobile").collection("ListingsAndReviews").findOne({Name :nameoflisting});
        res.writeHead(200, JSON.stringify(result));
        res.end();
        if (result) {
            
            console.log(`'${nameoflisting}'`);
            console.log(result);
        }else{
            console.log('no result to show')
        }
}}).listen(8080);
