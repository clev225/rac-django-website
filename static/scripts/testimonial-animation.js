document.addEventListener('DOMContentLoaded', function() {
    const testimonials = document.querySelectorAll('.col-md-10');
    let currentTestimonial = 0;
    
    // Initially hide all testimonials
    testimonials.forEach(testimonial => {
        testimonial.classList.add('hidden');
    });

    // Show first testimonial and preview of second
    testimonials[0].classList.remove('hidden');
    testimonials[0].classList.add('slide-in-fwd-bottom', 'current');
    if (testimonials[1]) {
        testimonials[1].classList.remove('hidden');
        testimonials[1].classList.add('preview');
    }

    // Handle scroll
    let isAnimating = false;
    window.addEventListener('wheel', function(e) {
        if (!isAnimating) {
            isAnimating = true;

            if (e.deltaY > 0 && currentTestimonial < testimonials.length - 1) {
                // Hide preview of next testimonial
                testimonials[currentTestimonial + 1].classList.remove('preview');
                // Hide current testimonial
                testimonials[currentTestimonial].classList.remove('current');
                testimonials[currentTestimonial].classList.add('hidden');
                
                // Show new current testimonial
                currentTestimonial++;
                testimonials[currentTestimonial].classList.remove('hidden');
                testimonials[currentTestimonial].classList.add('slide-in-fwd-bottom', 'current');
                
                // Show preview of next testimonial if available
                if (currentTestimonial < testimonials.length - 1) {
                    testimonials[currentTestimonial + 1].classList.remove('hidden');
                    testimonials[currentTestimonial + 1].classList.add('preview');
                }
                
                setTimeout(() => {
                    isAnimating = false;
                }, 400);
            } else if (e.deltaY < 0 && currentTestimonial > 0) {
                // Hide current preview if exists
                if (currentTestimonial < testimonials.length - 1) {
                    testimonials[currentTestimonial + 1].classList.add('hidden');
                    testimonials[currentTestimonial + 1].classList.remove('preview');
                }
                
                // Hide current testimonial
                testimonials[currentTestimonial].classList.remove('current');
                testimonials[currentTestimonial].classList.add('hidden');
                
                // Show previous testimonial
                currentTestimonial--;
                testimonials[currentTestimonial].classList.remove('hidden');
                testimonials[currentTestimonial].classList.add('slide-in-bck-top', 'current');
                
                // Show preview of next testimonial
                testimonials[currentTestimonial + 1].classList.remove('hidden');
                testimonials[currentTestimonial + 1].classList.add('preview');
                
                setTimeout(() => {
                    isAnimating = false;
                }, 600);
            } else {
                isAnimating = false;
            }
        }
    });
});