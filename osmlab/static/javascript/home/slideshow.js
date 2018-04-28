var slides = [];
var pips = [];
var currentSlide = 0;
var interval = -1;

function initializeSlideshow() {
  slideshowRoot = $('.home-header__slideshow');
  slides = $('.home-slide');
  createPips();
  resetTimers();
}

function resetTimers() {
  window.clearInterval(interval);
  interval = window.setInterval(rotateSlide, 5000);
}

function createPips() {
  var pipContainer = $('<div class="home-slide__pip-container"></div>');

  for (var i = 0; i < slides.length; i++) {
    var pip = $('<div class="home-slide__pip"></div>');

    if (i == 0) {
      pip.addClass('home-slide__pip--active');
    }

    pip.data('pipIndex', i);

    pipContainer.append(pip);
  }

  slideshowRoot.append(pipContainer);

  pips = $('.home-slide__pip');

  pips.on('click', function (event) {
    event.preventDefault();
    var index = $(this).data('pipIndex')
    currentSlide = index - 1;
    rotateSlide();
  });
}

function rotateSlide() {
  currentSlide = (currentSlide + 1) % slides.length;

  pips.removeClass('home-slide__pip--active');
  $(pips.get(currentSlide)).addClass('home-slide__pip--active');

  slides.each(function (index, slide) {
    slide.style.transform = 'translate3d(' + (-100 * currentSlide) + '%, 0, 0)';
  });

  resetTimers();
}

document.addEventListener('DOMContentLoaded', initializeSlideshow);
