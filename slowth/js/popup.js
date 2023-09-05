// This function creates an alarm set an minutes selected from the .html
function setAlarm() {
    var minutes = parseInt($("#time").val())
    chrome.alarms.create('reminderAlarm', {
        periodInMinutes: minutes
    })
    window.close()
}

// This function sets off the alarm when the user submits "off" from the .html
function setOff() {
    chrome.alarms.clear('reminderAlarm')
    window.close()
}

// Upon clicking submit, the alarm is set
$("#submit").click(setAlarm)

// Upon clicking "off", the alarm is set off
$("#off").click(setOff)