const kue = require('kue');
const redis = require('redis');
const { promisify } = require('util');
const express = require('express');
const app = express();

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.set("available_seats", 50);

let reservationEnabled = true;
function reserveSeat(number) {
    setAsync('available_seats', number.toString());
}

async function getCurrentAvailableSeats() {
    const seats = await getAsync("Available_seats");
    return parseInt(seats);
}

const queue = kue.createQueue();

app.get('/available_seats', async(req, res) => {
    const availableSeats = await getAsync('available_seats');
    res.json({ availableSeats });
});

app.get('/reserve_seat', async(req, res) => {
    if (reservationEnabled == false) {
        res.json({status: "Reservation are blocked"});
    }
    const job = queue.create('reserve_seat', {})
    .save(err => {
        if (err) res.json({status: "Reservation failed"});
        else res.json({status: "Reservation in process"});
    })
    .on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    })
    .on('failed', (err) => {
        console.log(`Seat reservation job ${job.id} failed: ${err}`);
    })
});

app.get('/process', async(req, res) => {
    const queue = kue.createQueue();
    queue.process('reserve_seat', async(job, done) => {
        const currentAvailableSeats = await getCurrentAvailableSeats();
        if (currentAvailableSeats <= 0) {
            reservationEnabled = false;
            return done(new Error('Not enough seats available'));
        }

        const newAvailableSeats = currentAvailableSeats - 1;
        await reserveSeat(newAvailableSeats);

        if (newAvailableSeats === 0) {
            reservationEnabled = false;
        }

        done();
    });

    res.json({status: "Queue processing"});
});


app.listen(1245, () => {
    console.log('Server is listening on port 1245');
});
