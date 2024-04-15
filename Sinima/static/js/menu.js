let navMainMenu = document.getElementById('nav-main-menu');
let secondaryMenu = document.getElementById('secondary-menu');
let mainMenu = document.getElementById('main-menu');
let userBar = document.getElementById('user-bar');
let openMenuBtn = document.getElementById('open-menu-btn');


function handleResize() {
    let windowWidth = window.screen.width;

    if (window.screen.width < 1200) {
        secondaryMenu.appendChild(navMainMenu);
        openMenuBtn.style.display = 'block';
        console.log(true);
    } else {
        // mainMenu.appendChild(navMainMenu);
        openMenuBtn.style.display = 'none';
        mainMenu.insertBefore(navMainMenu, userBar);
        console.log(false);
    }
}

window.addEventListener('resize', handleResize);

handleResize()

openMenuBtn.addEventListener('click', function () {

    console.log('Work')
    if (navMainMenu.dataset.open == 0) {
        navMainMenu.style.display = 'flex';
        navMainMenu.dataset.open = 1;
    } else if (navMainMenu.dataset.open == 1) {
        navMainMenu.style.display = 'none';
        navMainMenu.dataset.open = 0;
    }

})

