dayjs.extend(window.dayjs_plugin_utc)

document$.subscribe(function() {
    var timezone = document.getElementById("timezone")
    if (!!timezone) {
        timezone.innerText = Intl.DateTimeFormat().resolvedOptions().timeZone.replace("_", " ")
    };
    for (let timezone of document.getElementsByClassName("timezone")) {
        timezone.innerText = Intl.DateTimeFormat().resolvedOptions().timeZone.replace("_", " ")
    };
    for (let time of document.getElementsByTagName("time")) {
        let format = time.getAttribute("data-format");
        time.innerText = dayjs(time.dateTime).local().format(format !== null ? format : "MMMM D H:mm");
    };
});
