import kue from 'kue';

const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        return new Error('Jobs is not an array');
    }
    jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', jobData)
        .save((err) => {
            if (err) console.log(`Notification job ${job.id} failed: ${err}`);
            else console.log(`Notification job created: ${job.id}`);
        })
        .on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        })
        .on('failed', (err) => {
            console.log(`Notification job ${job.id} failed: ${err}`);
        })
        .on('progress', (err) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });
    });
}

export default createPushNotificationsJobs;
