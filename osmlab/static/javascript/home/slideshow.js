var slides = [];
var currentSlide = 0;

function initializeSlideshow() {
  slides = document.querySelectorAll('.home-slide');
  window.setInterval(rotateSlide, 5000);
}

function rotateSlide() {
  currentSlide = (currentSlide + 1) % slides.length;

  slides.forEach(function (slide) {
    slide.style.transform = 'translate3d(' + (-100 * currentSlide) + '%, 0, 0)';
  });
}

document.addEventListener('DOMContentLoaded', initializeSlideshow);
