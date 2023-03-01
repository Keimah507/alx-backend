import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

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

async function displaySchoolValue(schoolName) {
  try {
      const value = await getAsync(schoolName);
      console.log(`${value}`);
  } catch (err) {
      console.error(err);
  }
}

async function main() {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}

main();
