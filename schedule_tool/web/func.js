function genInputForm() {
    var min = document.getElementById("input-num").value
    var x = document.getElementById("input-position-x").value
    var y = document.getElementById("input-position-y").value
    console.log(min, x, y)
    eel.main(min, x, y)
}

function exitProcess() {
    eel.exit_()
}


async function processingStart() {
    var statusText = await eel.print_processing_status()()
    var div = document.getElementById("status-text")
    div.innerHTML = statusText
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

// function getMousePosition() {
//
//     if () {
//         var x = event.screenX;     // Get the horizontal coordinate
//         var y = event.screenY;     // Get the vertical coordinate
//         var coor = "X coords: " + x + ", Y coords: " + y;
//         var div = document.getElementById("position")
//         div.innerHTML = '<p>' + x + ', ' + y + '</p>'
//     }
//
// }