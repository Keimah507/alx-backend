import { createClient } from 'redis';
import redis from 'redis';
import { promisify } from 'util';


const client = createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);
  
client.on('ready', () => {
    console.log('Redis client connected to the server');
});
 
client.on('error', (err) => {
    console.log(`Redis client not connected to the server:${ err}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
};

function displaySchoolValue(schoolName) {
   client.get(schoolName, (err, value) => {
       if (err) {
           console.error(err);
       } else {
           console.log(`${value}`);
       }
});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
