function hamburger_nav() {
    var navLinks = document.getElementById('nav-links');
    if(navLinks.style.display === 'none')
      navLinks.style.display = 'block';
    else
      navLinks.style.display = 'none';
}

window.onscroll = function() {scrollFunction()};
let mybutton = document.getElementById("myBtn");
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
    var topBtn = document.getElementById(myBtn);
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}