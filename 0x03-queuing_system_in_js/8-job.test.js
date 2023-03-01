const kue = require('kue');
import sinon from 'sinon';
const { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('CreatePushNotificationsJobs', function() {

    before(() => {
        queue.testmode.enter();
    });

    after(() => {
        queue.testmode.exit();
    });

    afterEach(() => {
        queue.testmode.clear();
    });

    it('should throw an error if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an aray');
    });

    it('should create a job in the queue for each job in the jobs array', () => {
        const jobs = [ {phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account'},
            { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account'} ];

        const logSpy = sinon.spy(console, 'log');

        createPushNotificationsJobs(jobs, queue);
        expect(logSpy.calledWith('Notification job created:')).to.be.true;

        logSpy.restore();
    });

    it('should log a message when a job is completed', async () => {
        const jobs = [ {phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account'},
            { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account'} ];
        const logSpy = sinon.spy(console, 'log');

        createPushNotificationsJobs(Jobs,queue);

        await new Promise(resolve => setTimeout(resolve, 1000));

        expect(logSpy.calledWith('Notification job completed')).to.be.true;

        logSpy.restore();
    });
    
    it('should log a message when a job fails', async () => {
        const jobs = [
            {
       phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
            },
            {
       phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
            },
            {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
            },
        ]
        const logSpy = sinon.spy(console,'log');

        jobs[0].phoneNumber = 'invalid';

        createPushNotificationsJobs(jobs, queue);

        await new Promise(resolve => setTimeout(resolve, 1000));

        expect(logSpy.calledWith('Notification job failed:')).to.be.true;

        logSpy.restore();
    });
});
