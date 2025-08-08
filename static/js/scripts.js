let currentIndex = 0;
const images = document.querySelectorAll('.img');
const totalImages = images.length;

const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const imageList = document.querySelector('.list');

// Function to move to the previous image
prevBtn.addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
    } else {
        currentIndex = totalImages - 1; // Wrap around to the last image
    }
    updateSlider();
});

// Function to move to the next image
nextBtn.addEventListener('click', () => {
    if (currentIndex < totalImages - 1) {
        currentIndex++;
    } else {
        currentIndex = 0; // Wrap around to the first image
    }
    updateSlider();
});

// Update the slider position
function updateSlider() {
    imageList.style.transform = `translateX(-${currentIndex * 100}%)`;
}


   function scrollSlider(direction) {
      const slider = document.getElementById("sliderList");
      const scrollAmount = slider.clientWidth;
      slider.scrollBy({ left: direction * scrollAmount, behavior: "smooth" });
    }

