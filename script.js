// make a programm that runs every 5 minutes and getPing, downloadSpeed, websiteLoadTime,  Upload speed, Jitter, Packet loss, DNS lookup time, Page load time, Availability, Throughput and returns it to the flask server
// we will test on multiple websites [google.com, classroom.google.com, mail.google.com, isak.managebac.com, drive.google.com, docs.google.com]

// Path: script.js


setInterval(function() {
    collectData();
}, 300000);

var websites = ["google.com", "classroom.google.com", "mail.google.com", "isak.managebac.com", "drive.google.com", "docs.google.com"];

function collectData() {
    var data = {
        "ping": getPing(),
        "downloadSpeed": getDownloadSpeed(),
        "websiteLoadTime": getWebsiteLoadTime(),
        "uploadSpeed": getUploadSpeed(),
        "jitter": getJitter(),
        "packetLoss": getPacketLoss(),
        "dnsLookupTime": getDNSLookupTime(),
        "pageLoadTime": getPageLoadTime(),
        "availability": getAvailability(),
        "throughput": getThroughput()
    }
    sendData(data);
}

 