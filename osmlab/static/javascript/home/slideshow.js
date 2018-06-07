var slideshowRoot, slides, pips, arrows;
var currentSlide = 0;
var interval = -1;

function initializeSlideshow() {
  slideshowRoot = $('.home-header__slideshow');

  if (!slideshowRoot || slideshowRoot.length === 0) {
    return;
  }

  slides = $('.home-slide');

  pipContainer = $('.home-slide__pip-container');
  if (pipContainer.length > 0) createPips();

  arrows = $('.home-slide__arrow');
  if (arrows.length > 0) createNavArrows();

  resetTimers();
}

function resetTimers() {
  window.clearInterval(interval);
  interval = window.setInterval(function() {
    incrementSlideIndex(1);
    animateSlides();
  }, 5000);
}

// Sets the current slide index to a new index given a delta.
// For example, you could pass in -2 to move back 2 slides.
function incrementSlideIndex(delta) {
  var newCurrentSlide = (currentSlide + delta) % slides.length;

  if (newCurrentSlide < 0) {
    currentSlide = slides.length - 1;
  } else {
    currentSlide = newCurrentSlide;
  }
}

function createNavArrows() {
  var leftArrow = $('.home-slide__arrow--left')
    .on('click', function (event) {
      event.preventDefault();
      resetTimers();
      incrementSlideIndex(-1);
      animateSlides();
    });
  var rightArrow = $('.home-slide__arrow--right')
    .on('click', function (event) {
      event.preventDefault();
      resetTimers();
      incrementSlideIndex(1);
      animateSlides();
    });
}

function createPips() {
  $.map(Array(3), function (_, index) {
    var pip = index === 0
      ? $('<div class="home-slide__pip home-slide__pip--active"></div>')
      : $('<div class="home-slide__pip"></div>');

    pip.data('pipIndex', index);
    pipContainer.append(pip);
  });
  pips = $('.home-slide__pip');

  pips.on('click', function (event) {
    event.preventDefault();
    resetTimers();
    var index = $(this).data('pipIndex')
    currentSlide = index;
    animateSlides();
  });
}

function animateSlides() {
  pips.removeClass('home-slide__pip--active');
  $(pips.get(currentSlide)).addClass('home-slide__pip--active');

  slides.each(function (index, slide) {
    slide.style.transform = 'translate3d(' + (-100 * currentSlide) + '%, 0, 0)';
  });
}

// Initialize content on DOM ready
$(function() {
  initializeSlideshow();
});
