// var connection =  require('./demo.js');
import { sourceFile } from './demo';
database = sourceFile.client
// console.log(variableName)
// results = database.client;
// console.log(results);
async function listdatabase(database){
    const data = await database.db().admin().listDatabases();
    data.databases.forEach(db => {
        console.log(`- ${db.name}`);
    })
}
// listdatabase().catch(console.error());
module.exports = listdatabase