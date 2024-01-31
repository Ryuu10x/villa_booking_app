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
      document.getElementById(roomType).style.display = "grid";

      // marking the clicked tab as selected
      event.currentTarget.classList.add("selected");
    });
  });
}

// function to handle the opening of the menu and booking
function OpenPopUp() {
  // menu
  document.getElementById("menu_button").addEventListener("click", function () {
    document.getElementById("menu_modal").style.display = "block";
  });

  // booking
  const bookingButtons = document.querySelectorAll("button.booking_button");

  bookingButtons.forEach(bookingButton => {
    bookingButton.addEventListener("click", function () {
      document.getElementById("booking_modal").style.display = "block";
      document.getElementById("menu_modal").style.display = "none";
    });
  });
}

// function to handle the closing of the menu and booking
function ClosePopUp() {
  const closeButtons = document.querySelectorAll("a.close_button");

  closeButtons.forEach(closeButton => {
    closeButton.addEventListener("click", function () {
      document.getElementById("menu_modal").style.display = "none";
      document.getElementById("booking_modal").style.display = "none";
    });
  });
}

document.addEventListener("DOMContentLoaded", function () {
  RoomTabs();
  OpenPopUp();
  ClosePopUp();
});

gsap.registerPlugin(ScrollTrigger);

jQuery(document).ready(function ($) {
  const isDesktop = window.innerWidth >= 1024;

  // gsap.to(".villa-image-1", {
  //     scrollTrigger: {
  //       trigger: ".gallery",
  //       start: "top center",
  //       end: "bottom top",
  //       scrub: 2,

  //     //   onEnter: () => {
  //     //     gsap.to(".villa-image-1", { opacity: 1 });
  //     //   },
  //     },
  //     y: isDesktop ? -50 : -50,
  //   });

  gsap.to(".villa-image-1", {
    scrollTrigger: {
      trigger: ".about_us",
      start: "top center",
      end: "bottom top",
      scrub: 2,

      onEnter: () => {
        gsap.to(".villa-image-1", { opacity: 1 });
      },
    },
    y: isDesktop ? -10 : -10,
  });

  gsap.to(".villa-image-2", {
    scrollTrigger: {
      trigger: ".about_us",
      start: "top center",
      end: "bottom top",
      scrub: 2,

      onEnter: () => {
        gsap.to(".villa-image-2", { opacity: 1 });
      },
    },
    y: isDesktop ? -50 : -50,
  });

  gsap.to(".villa-image-3", {
    scrollTrigger: {
      trigger: ".about_us",
      start: "top center",
      end: "bottom top",
      scrub: 2,

      onEnter: () => {
        gsap.to(".villa-image-3", { opacity: 1 });
      },
    },
    y: isDesktop ? -20 : -20,
  });

  gsap.to(".villa-image-4", {
    scrollTrigger: {
      trigger: ".about_us",
      start: "top center",
      end: "bottom top",
      scrub: 2,

      onEnter: () => {
        gsap.to(".villa-image-4", { opacity: 1 });
      },
    },
    y: isDesktop ? -30 : -30,
  });
  gsap.to(".background_text", {
    scrollTrigger: {
      trigger: ".about_us",
      start: "top center",
      end: "bottom top",
      scrub: 2,

      onEnter: () => {
        gsap.to(".background_text", { opacity: 0.4 });
      },
    },
    y: isDesktop ? -50 : -50,
  });

  gsap.to(".room_info", {
    scrollTrigger: {
      trigger: ".rooms",
      start: "top bottom",
      end: "top top",
      scrub: 2,

      //   onEnter: () => {
      //     gsap.to(".others", { opacity: 1 });
      //   },
    },
    y: isDesktop ? 0 : 0,
    opacity: 1,
  });

  gsap.to(".others", {
    scrollTrigger: {
      trigger: ".others",
      start: "top bottom",
      end: "top center",
      scrub: 2,

      //   onEnter: () => {
      //     gsap.to(".others", { opacity: 1 });
      //   },
    },
    y: isDesktop ? 0 : 0,
    opacity: 1,
  });


})