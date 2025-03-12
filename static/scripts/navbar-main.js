document.addEventListener('DOMContentLoaded', function() {
    // Load the navbar component
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'components/navbar-main.html', true);
    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            var navbarPlaceholder = document.getElementById('navbar-placeholder');
            navbarPlaceholder.innerHTML = this.responseText;

            // Set active class based on current page
            const currentPage = window.location.pathname.split('/').pop() || 'index.html';
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

            navLinks.forEach(link => {
                const linkPage = link.getAttribute('href');
                // Remove any existing active class and bold style
                link.classList.remove('active');
                link.style.fontWeight = 'normal';
                
                // Check if this link matches the current page
                if (linkPage === currentPage || 
                    (currentPage === '' && linkPage === 'index.html') ||
                    (currentPage === '/' && linkPage === 'index.html')) {
                    link.classList.add('active');
                    link.style.fontWeight = 'bold';
                }
            });

            // Load the modal component
            var xhrModal = new XMLHttpRequest();
            xhrModal.open('GET', 'components/modal.html', true);
            xhrModal.onreadystatechange = function() {
                if (this.readyState === 4 && this.status === 200) {
                    // Create a temporary div to hold the modal content
                    const tempDiv = document.createElement('div');
                    tempDiv.innerHTML = this.responseText;
                    document.body.appendChild(tempDiv);

                    const navbarToggler = document.querySelector('.navbar-toggler');
                    const navbarPopover = document.querySelector('.navbar-popover');
                    const closeBtn = document.querySelector('.close-btn');

                    if (!navbarToggler || !navbarPopover || !closeBtn) {
                        console.error('Required navbar elements not found');
                        return;
                    }

                    // Function to show the popover
                    function showPopover(event) {
                        event.preventDefault();
                        event.stopPropagation();
                        navbarPopover.style.display = 'flex';
                        requestAnimationFrame(() => {
                            navbarPopover.classList.add('show');
                        });
                    }

                    // Function to hide the popover
                    function hidePopover() {
                        navbarPopover.classList.remove('show');
                        setTimeout(() => {
                            navbarPopover.style.display = 'none';
                        }, 300); // Match this with your CSS transition duration
                    }

                    // Initially hide the popover
                    navbarPopover.style.display = 'none';

                    // Remove any existing event listeners
                    navbarToggler.replaceWith(navbarToggler.cloneNode(true));
                    navbarToggler = document.querySelector('.navbar-toggler');

                    // Add click event listener to navbar toggler
                    navbarToggler.addEventListener('click', showPopover);

                    // Close the modal when clicking outside of it
                    document.addEventListener('click', function(event) {
                        if (navbarPopover.style.display !== 'none' && 
                            !navbarPopover.contains(event.target) && 
                            event.target !== navbarToggler) {
                            hidePopover();
                        }
                    });

                    // Close the modal when clicking the close button
                    closeBtn.addEventListener('click', hidePopover);

                    // Prevent clicks inside the popover from closing it
                    navbarPopover.addEventListener('click', function(event) {
                        event.stopPropagation();
                    });
                }
            };
            xhrModal.send();
        }
    };
    xhr.send();
});
