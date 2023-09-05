# SLOWTH
## Video Demo:  <URL HERE>
## Description:

My final project for CS50 is a Google Chrome extension called "Slowth" which takes the word "slow" and the word for the mammal "sloth" and puts them together to create the extension's name. Just as a sloth would do, the extension is a set-reminder tool for the user to slow down during a work session and take a break.

The idea was born after I spent countless hours at my job staring at my screen and forgetting to take a break. This caused me eye and mental fatigue, back pain and a sense of overwhelmeness. With this in mind, and considering the Pomodoro technique that devides work sessions in 25min interval and 5min rest, I decided to create Slowth.

During the planning stage, I considered building a web-application for Slowth; however, I soon realized that having one more tab opened in the user's browser would only caused inconvenience. First, because the user will occupy one more space in his tab section and, second, going back to tab to set a new slowth session or turning it off is impractical. Therefore, a Chrome extension, or any sort of extension, was the best way to put my idea in practice.

The challenge ahead was to learn to learn to create a Google extension using JavaScript, Google Chrome's alarms API and having an appealing, yet easy, UI. For that, I decided to read Chrome's documentation on alarms and notifications as well as watching YouTube tutorials on these same topics.

My directiory /slowth contains two folders and three other files, all organized according to the documentation on creating a Google Chrome extension. I will proceed on to explain each folder and each file in turn.

### **Manifest.json**
The manifest.json is the spinal document for creating a Google Chrome extension. It contains imporant information for running the extension such as its description, installation, background scripts that add funcionality, permissions for APIs to be used in the logic of the extension, any user interface .html documents and icons.

The manifest.json for Slowth contains the manifest 3 version that runs underneath the extension. I added permissions for Chrome's established APIs notifications and alarms. I added a "background" that listens for the creation of an alarm and then triggers a notification. Finally, an "action" was added that takes an .html pop-up where the user creates an alarm that creates notifications.

### **Popup.html**
The popup.html is our User Interface where the user is asked to set an alarm that will trigger a notification according to the time, in minutes, provided to the UI. The tools used for this file was html, CSS and JavaScript language. However, the JS for the logic of the front-end was written in separate files that were then referenced within the popup.html.

The UI is simple. It contains an input tag where the user can type or select the interval in minutes in which the notification will be triggered. Two button tags are provided. The _Update_ button sets the alarm while the _Off_ button clears the alarm so that the user can set it off.

### **/js Directory**
The /js directory contains three documents that are the logic of Slowth Chrome extension: a background.js, a jquery.js and a popup.js.

## jquery.js
The jquery.js is our JavaScript library loaded to our directory to work with a less rubost language and simplify tasks that would otherwise take many lines of code to be accomplished.

## Background.js
The background.js is a key component of the logic of Slowth. It listens on the background for the creation of an alarm on the popup.html via the popup.js file so that it can create a notification that then will be triggered according to the user's preference.

## Popup.js
The popup.js is the logic behind the popup.html. First, it cretes a function called _setAlarm_ to set a new alarm that takes the number provided by the user via the UI, getting the element "#time", and passes it to a variable called _minutes_ and then creates an alarm with Chrome.alarms API that passes _minutes_ as its argument. Once the alarm is created, the background.js listens for it and triggers a notification according to the _minutes_ variable.

A second function called _setOff_ takes the alarm already running and _clears_ it so that the user can set the alarm off via UI.

Popup.js gets elements by ID from the popup.html to both set the alarm or set it off. It listens for a click on either the element "#submit" or "#off" in the popup.html and calls on _setAlarm_ or _setOff_ functions accordingly.

### **/img Directory**
Finally, the /img directory contains all the images used for the front-end of our application. The images were obtained on the open source site https://www.flaticon.com/free-icons/sloth. The sloth icons, here named for the purpose of the Chrome extention sloth_16.png, sloth_32.png and sloth_128.png were created by the user  Freepik. Here I include links to the icons for the respective credit and great contribution to the Slowth project.

<a href="https://www.flaticon.com/free-icons/sloth" title="sloth icons">Sloth icons created by Freepik - Flaticon</a>

### **Final remarks**
The next step in the process for Slowth is to add more logic so that I can include the pomodoro technique, developed by Francesco Cirillo, within the extension so that it not only reminds users when to slowth(take a break), but also sets time slots to rest. Furthermore, I would love to add with each notification, some suggestion as to how to best rest for that interval of time.

Thank you to CS50, professor David J. Malan and all his team for providing with the world with this essential and incredible resource for us who had never befored code and want to venture into the world of IT. I am forever grateful to the University of Hardvard, which I once visited during a conference, and to Yale University for providing this class for free via edX, and special thanks to edX for developing this tool for free education from leading universities in the world. The impact in education all the above actors mentioned are doing is beyond the imaginable.