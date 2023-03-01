const redis = require('redis');
const { promisify }  =  require('util');
const express = require('express');
const app = express();

const listProducts = [
    { id: 1,
        name: 'Suitcase 250',
        price: 50,
        stock: 4
    },
    { id: 2,
        name: 'Suitcase 450',
        price: 100,
        stock: 10
    },
    { id: 3,
        name: 'Suitcase 650',
        price: 350,
        stock: 2,
    },
    { id: 4,
        name: 'Suitcase 1050',
        price: 550,
        stock: 5
    }
]

function getItemById(id) {
    return listProducts.find(x => x.id === id);
}

app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

app.get('/list_products/:itemId', async(req, res) => {
    try {
        const itemId = req.params.itemId;
        const product = getItemById(itemId);
        const curr_stock = await getCurrentReservedStockById(ItemId);
        response.json({...product, curr_stock });
    } catch (err) {
    res.json({status: "Product not Found"});
}
});

app.get('/reserve_product/:itemId', async(req, res) => {
    try {
        const itemId = req.params.itemId
        const curr_stock = await getCurrentReservedStockById(itemId);
        if (stock <= 0) {
            res.json({status: "Not enough stock available", itemId});
        } else {
            await reserveStockById(itemId, curr_stock - 1);
            res.send({status: "Reservation confirmed", itemId});
        }
    } catch {
        res.json({ status: 'Product not found' });
    }
});

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('ready', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server:${ err}`);
});

function reserveStockById(itemId, stock) {
    setAsync(`item.${item.id}`, stock);
}

async function getCurrentReservedStockbyId(itemId) {
    try {
        const stockId = await reserveStockById(`item.${item.id}`);
        return parseInt(stockId) || 0;
    } catch (err) {
        console.error(err);
    }
}
app.listen(1245);
