function getGroupUrl() {
    const url_list = []
    const urls = document.getElementsByName("group_url")
    const urls_len = urls.length

    for (let i = 0; i < urls_len; i++) {
        url_list.push(urls[i].value)
    }
    processingStart()
    eel.main(url_list)
    processingEnd()
}


function genInputForm() {
    var num = document.getElementById("input-num").value;
    var form = "<form class='input-form'><label>社團網址:</label><br>"

    for (var i = 0; i < num; i++) {
        form += "<input class='input-area' type='text' name='group_url' placeholder='請輸入社團網址'><br>"
    }
    form += "<button type='button' class='btn' onclick='getGroupUrl()'>Enter</button>"
    form += "</form>"
    var div = document.getElementById("form-part")
    div.innerHTML = form
}


async function processingStart() {
    var statusText = await eel.print_processing_status()()
    var div = document.getElementById("status-text")
    div.innerHTML = statusText
}


async function processingEnd() {
    var statusText = await eel.print_ending_status()()
    var div = document.getElementById("status-text")
    div.innerHTML = statusText
}
