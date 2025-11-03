document.addEventListener("DOMContentLoaded", function() {
    // Select all carousel items
    const carouselItems = document.querySelectorAll('.carousel-item');

    // Check if there are any items
    if (carouselItems.length > 0) {
        // Add the 'active' class to the first item
        carouselItems[0].classList.add('active');
    }
});