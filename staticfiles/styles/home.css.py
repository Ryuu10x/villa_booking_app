/* :root {
    --primary-color: #3498db;
    --secondary-color: #2ecc71;
    --accent-color: #e67e22;
    --text-color: #333;
    --background-color: #f5f5f5;
} */

/* universal */

* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: 'Poppins';
}

a {
    color: white;
}

a:link {
    text-decoration: none;
}

.main_container {
    width: 90%;
    margin: auto;
    max-width: 1200px;
}

header {
    background-color: lightseagreen;
    padding: 10px 0;
}

header .main_container {
    display: flex;
    justify-content: space-between;
}

.logo_container {
    display: flex;
}

.logo_container h2 {
    color: white;
    font-weight: normal;
    font-size: 20px;
    padding: 5px;
}

.logo {
    width: 40px;
    height: 40px;
    position: relative;
    overflow: hidden;
    border-radius: 50%;
}

.logo img {
    display: inline;
    margin: 0 auto;
    margin-left: -25%;
    height: 100%;
    width: auto;
}

.menu_tabs {
    display: none;
}

/* menu modal */
#menu_modal .main_container,
#booking_modal .main_container {
    max-width: 400px;
}

#menu_button {
    font-size: 30px;
    padding: 3.5px;
    display: block;
}

#menu_button div {
    width: 30px;
    height: 3px;
    background-color: white;
    margin: 6px 0;
}

.dimmer {
    height: 100%;
    width: 100%;
    display: none;
    position: fixed;
    z-index: 1;
    background-color: rgba(0, 0, 0, 0.7);
}

.overlay {
    /* height: 280px; */
    /* width: 280px; */
    position: fixed;
    z-index: 2;
    top: 50%;
    left: 50%;
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    background-color: white;
    border-radius: 5px;
    padding: 50px 20px 30px 20px;
}

.overlay-content {
    position: relative;
    top: 25%;
    width: 100%;
    text-align: center;
}

.overlay-content .transparent_button {
    color: black;
}

.overlay-content a {
    width: 50%;
    margin: auto;
}

.overlay-content button {
    margin-top: 5px;
    border: 2px solid black;
}

.overlay a {
    padding: 8px;
    text-decoration: none;
    color: black;
    font-weight: bold;
    display: block;
    margin-bottom: 20px;
}

.overlay a:hover,
.overlay a:focus {
    color: lightseagreen;
    border-bottom: 2px solid lightseagreen;
}

.overlay button {
    font-weight: bold;
}

.overlay .close_button {
    position: absolute;
    top: 20px;
    right: 20px;
    font-size: 20px;
    color: white;
    background-color: black;
    border-radius: 20px;
    padding: 0px 8px;
}

/* book now modal */
#booking_modal .overlay-content>* {
    margin: 20px 0;
}

#start,
#end,
#villa_type {
    width: 200px;
}

#booking_modal input,
#booking_modal select {
    border: 2px solid black;
    display: block;
    margin: auto;
}

#booking_modal input:focus,
#booking_modal select:focus {
    outline: none;
}

#booking_modal .overlay-content div label {
    margin: 10px 20px;
    display: block;
}

#villa_type {
    appearance: none;
    background-image:
        linear-gradient(45deg, transparent 50%, gray 50%),
        linear-gradient(135deg, gray 50%, transparent 50%),
        radial-gradient(#ddd 70%, transparent 72%);
    background-position:
        calc(100% - 20px) calc(1em + 2px),
        calc(100% - 15px) calc(1em + 2px),
        calc(100% - .5em) .5em;
    background-size:
        5px 5px,
        5px 5px,
        1.5em 1.5em;
    background-repeat: no-repeat;
    padding: 10px 40px 10px 25px;
}

#villa_type:focus {
    background-image:
        linear-gradient(45deg, white 50%, transparent 50%),
        linear-gradient(135deg, transparent 50%, white 50%),
        radial-gradient(gray 70%, transparent 72%);
    background-position:
        calc(100% - 15px) 1em,
        calc(100% - 20px) 1em,
        calc(100% - .5em) .5em;
    background-size:
        5px 5px,
        5px 5px,
        1.5em 1.5em;
    background-repeat: no-repeat;
}

#book_button {
    padding: 10px 45px;
    border: none;
}

/* introduction */
.hero .transparent_button {
    margin: 20px 0;
}

.hero .main_container {
    position: relative;
    width: 90%;
    height: 500px;
}

.container {
    background-image: url('{% static "image/villa_image_1.avif" %}');
    background-position: center;
    background-size: cover;
    position: relative;
    width: 100%;
    height: 500px;
}

.tint {
    background-color: rgba(18, 96, 92, 0.6);
    background-blend-mode: multiply;
}

.context {
    width: 100%;
    top: 50%;
    left: 50%;
    position: absolute;
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    text-align: center;
}

.context>* {
    /* margin: 20px; */
    font-weight: bold;
    color: white;
}

.context p {
    font-size: 30px;
    line-height: 150%;
}

.transparent_button {
    border: 2px solid white;
    background-color: transparent;
    font-size: 15px;
    border-radius: 25px;
    color: white;
    transition: all 0.2s ease-in-out;
    cursor: pointer;
}

.transparent_button:hover {
    background-color: white;
    color: black;
    font-weight: 600;
}

.horizontal_rounded_edges {
    padding: 10px 25px;
}

.vertical_rounded_edges {
    padding: 15px 10px;
}

/* About Us */
.about_us {
    position: relative;
}

.about_us>* {
    margin: 15px 0;
}

.about_us_section {
    margin-bottom: 10px;
}

.about_us_section>* {
    margin: 15px 0;
}

.about_us_section p {
    line-height: 150%;
}

.solid_button {
    background-color: lightseagreen;
    color: white;
    font-size: 15px;
    border-radius: 25px;
    cursor: pointer;
    border: none;
    transition: all 0.2s ease-in-out;
}

.solid_button:hover {
    background-color: rgb(43, 213, 205);
}

.background_text {
    position: absolute;
    top: 50%;
    left: 50%;
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    z-index: -1;
    color: lightseagreen;
    opacity: 20%;
    font-size: 100px;
    font-weight: bold;
    text-align: center;
    line-height: 90%;
    opacity: 0;
}

.gallery {
    display: grid;
    grid-template-columns: 0.3fr 0.4fr 0.3fr;
    grid-gap: 5px;
}

.gallery img {
    max-width: 100%;
    height: 100%;
    border-radius: 5px;
}

.gallery div.about_us_section:nth-child(1) {
    grid-column-start: 1;
    grid-column-end: 4;
    grid-row-start: 1;
    grid-row-end: 2;
}

.gallery img:nth-child(2) {
    grid-column-start: 1;
    grid-column-end: 3;
    grid-row-start: 2;
    grid-row-end: 3;
}

.gallery img:nth-child(3) {
    grid-column-start: 3;
    grid-column-end: 4;
    grid-row-start: 2;
    grid-row-end: 3;
}

.gallery img:nth-child(4) {
    grid-column-start: 1;
    grid-column-end: 2;
    grid-row-start: 3;
    grid-row-end: 4;
}

.gallery img:nth-child(5) {
    grid-column-start: 2;
    grid-column-end: 4;
    grid-row-start: 3;
    grid-row-end: 4;
}

/* Room Details */
.room_tabs {
    width: 288px;
    display: flex;
    background-color: white;
    border-radius: 20px;
    justify-content: center;
    margin: auto;
}

.tab_button {
    background: transparent;
    font-weight: bold;
    font-size: 12.5px;
    border-radius: 20px;
    padding: 10px 7.5px;
    border: none;
    cursor: pointer;
}

.tab_button:active,
.selected {
    background-color: lightseagreen;
    color: white;
}

#silver,
#gold {
    display: none;
}

.rooms {
    text-align: center;
    padding: 20px 0 5px 0;
    background-color: rgb(235, 235, 235);
}

.room_info {
    margin: 10px 0;
    place-items: center;
    transform: translateY(50px);
    opacity: 0;
}

.room_info_container>*>* {
    margin: 10px 0;
}

.room_info_container img {
    width: 100%;
    border-radius: 5px;
    /* text-align: center; */
}

.room_info_container h2 {
    font-size: 22px;
    margin-bottom: 20px;
}

.room_info_container p {
    text-align: left;
}

.room_info_pic {
    max-width: 500px;
}

.room_details {
    width: 90%;
    display: flex;
    margin: 20px auto 5px auto;
    justify-content: center;
    border-radius: 25px;
    border: 2px solid lightseagreen;
    padding: 10px;
}

.room_details>* {
    margin: 0 8px;
    font-weight: bold;
}

.dimension,
.people {
    color: lightseagreen;
}

.price {
    color: rgb(218, 186, 4);
}

/* Others */
.others {
    padding: 20px 0;
    opacity: 0;
    transform: translateY(50px);
}

.others .container {
    /* width: auto; */
    max-width: 500px;
    height: 450px;
    margin: 20px auto;
    border-radius: 5px;
}

.others .container p {
    font-size: 15px;
    max-width: 250px;
    margin: auto;
}

/* Footer */
footer {
    background-color: lightseagreen;
    padding: 10px 0;
    color: white;
}

footer>*>* {
    margin: 30px 0;
}

footer>*>*>* {
    margin-bottom: 20px;
}

footer>*>* p {
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.contact_info svg {
    font-size: 30px;
}

.socials>*>* {
    margin-right: 10px;
    width: 40px;
}

.credit {
    display: flex;
    justify-content: center;
    margin-bottom: 0px;
}

.context-details {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, calc(-50% + 100px));
    width: 100%;
    opacity: 0;
    pointer-events: none;
    transition: all 0.2s ease-in-out;

}

.context-details button {
    margin-top: 20px;
}

.context-details p {
    font-weight: 500;
}

.others-content {
    position: relative;

}

.others-content .context h2 {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    transition: all 0.2s ease-in-out;
}

.others-content:hover .context h2 {
    transform: translate(-50%, calc(-50% - 100px));
}

.others-content:hover .context-details {
    transform: translate(-50%, -50%);
    opacity: 1;
    pointer-events: auto;
}

.animate-arrow-container {
    padding: 15px 5px;
}

.animate-arrow {
    /* font-size: 16px; */
    /* font-weight: 800; */
    animation: bounce 2s ease-in-out infinite;
    translate: 0 -5px;
    display: inline-block;
    rotate: 180deg;
}

.animate-arrow svg {
    font-size: 20px;
}

@keyframes bounce {
    0% {
        transform: translateY(-10px);
    }

    50% {
        transform: translateY(0);
    }

    /* 75%{
        transform: translateY(5px);
    } */
    100% {
        transform: translateY(-10px);
    }
}

/* For Desktop */
@media only screen and (min-width: 1024px) {
    #booking_modal .overlay-content div {
        width: 100%;
        display: flex;
        justify-content: space-between;
    }

    #booking_modal input,
    #booking_modal select {
        margin: 0;
    }

    #menu_button {
        display: none;
    }

    .menu_tabs {
        display: block;
        padding: 2.5px 0;
    }

    .menu_tabs>* {
        margin: 0 15px;
        font-size: 14px;
    }

    .menu_tabs button {
        padding: 5px 15px;
        color: white;
    }

    .context p {
        max-width: 500px;
        margin: auto;
    }

    .gallery {
        display: grid;
        grid-template-columns: 0.47fr 0.06fr 0.22fr 0.05fr 0.22fr;
        grid-template-rows: 0.01fr 0.07fr 0.07fr 0.05fr 0.45fr 0.35fr;
        grid-gap: 5px 15px;
        margin: 40px 0;
    }

    .gallery img {
        width: 100%;
        height: 100%;
        border-radius: 5px;
    }

    .gallery div.about_us_section:nth-child(1) {
        grid-column-start: 3;
        grid-column-end: 6;
        grid-row-start: 1;
        grid-row-end: 2;
    }

    .gallery img:nth-child(2) {
        grid-column-start: 1;
        grid-column-end: 2;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .gallery img:nth-child(3) {
        grid-column-start: 4;
        grid-column-end: 6;
        grid-row-start: 2;
        grid-row-end: 6;
    }

    .gallery img:nth-child(4) {
        grid-column-start: 3;
        grid-column-end: 5;
        grid-row-start: 4;
        grid-row-end: 7;
    }

    .gallery img:nth-child(5) {
        grid-column-start: 1;
        grid-column-end: 3;
        grid-row-start: 5;
        grid-row-end: 7;
    }

    .room_info {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px;
        /* place-items: center; */
        /* justify-content: flex-start; */
        place-items: unset;
        align-items: center;
    }

    .room_info_container h2 {
        text-align: left;
    }

    .room_details {
        width: fit-content;
        margin: 0;
    }

    .room-details-btn-container {
        display: flex;
        gap: 20px;
    }

    .room-details-btn-container {
        margin-top: 20px;
    }

    .room_tabs {
        margin: 0;
        margin-bottom: 20px;
    }

    .others {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        opacity: 0;
        transform: translateY(50px);
    }

    footer .main_container {
        display: flex;
        /* align-items: center; */
        justify-content: space-between;
    }
}