// function to handle the room tabs in the home page
function RoomTabs() {
    var tabs = Array.from(document.getElementsByClassName("tab_button"));
    tabs.forEach(tab => {
        tab.addEventListener("click", function (event) {
            // removing all the room info
            var rooms = document.getElementsByClassName("room_info");
            for (var i = 0; i < rooms.length; i++) {
                rooms[i].style.display = "none";
            }

            // resetting the tabs
            tabs.forEach(t => t.classList.remove("selected"));

            // displaying the clicked room info
            var roomType = tab.getAttribute("data-room-type");
            document.getElementById(roomType).style.display = "block";

            // marking the clicked tab as selected
            event.currentTarget.classList.add("selected");
        });
    });
}

// function to handle the opening of the menu
function OpenMenu() {
    document.getElementById("menu_button").addEventListener("click", function () {
        document.getElementById("menu").style.display = "block";
        document.getElementById("dimmer").style.display = "block";
    });
}

// function to handle the closing of the menu
function CloseMenu() {
    document.getElementById("close_button").addEventListener("click", function () {
        document.getElementById("menu").style.display = "none";
        document.getElementById("dimmer").style.display = "none";
    });
}

document.addEventListener("DOMContentLoaded", function () {
    RoomTabs();
    OpenMenu();
    CloseMenu();
});