'use strict';

chrome.alarms.onAlarm.addListener(function() {
    chrome.notifications.create({
        type: 'basic',
        iconUrl: '/img/sloth_128.png',
        title: 'Break!',
        message: 'Take a slowth break!',
        priority: 0});
});