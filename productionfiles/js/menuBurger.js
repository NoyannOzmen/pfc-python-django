const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector("#nav-links");
const navLink = document.querySelectorAll(".item-link");

hamburger.addEventListener("click", mobileMenu);
hamburger.addEventListener("keydown", function(e) {
    if(e.keyCode==13){
      mobileMenu();
     }
  });
navLink.forEach(n => n.addEventListener("click", closeMenu));
navLink.forEach(n => n.addEventListener("keydown", function(e) {
    if(e.keyCode==13){
      closeMenu();
     }
  }))

function mobileMenu() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
}

function closeMenu() {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
}