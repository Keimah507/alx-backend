import { createClient } from 'redis';
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
