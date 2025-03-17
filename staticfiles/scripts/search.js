function searchServices() {
    const searchInput = document.getElementById('serviceSearch');
    const searchText = searchInput.value.toLowerCase();
    const serviceRows = document.querySelectorAll('.service-row');
    const noResultsDiv = document.getElementById('noResults');
    let hasVisibleServices = false;

    serviceRows.forEach((row, index) => {
        const serviceTitle = row.querySelector('.service-title').textContent.toLowerCase();
        const serviceText = row.nextElementSibling;
        const isVisible = serviceTitle.includes(searchText);
        
        if (isVisible) {
            hasVisibleServices = true;
            // Show with popup animation
            row.style.transition = 'all 0.3s ease-out';
            row.style.transform = 'scale(0.95)';
            row.style.opacity = '0';
            row.style.display = 'flex';
            
            setTimeout(() => {
                row.style.transform = 'scale(1)';
                row.style.opacity = '1';
            }, index * 100); // Staggered delay based on index

            if (serviceText && serviceText.classList.contains('service-text')) {
                serviceText.style.transition = 'all 0.3s ease-out';
                serviceText.style.transform = 'scale(0.95)';
                serviceText.style.opacity = '0';
                serviceText.style.display = 'block';
                
                setTimeout(() => {
                    serviceText.style.transform = 'scale(1)';
                    serviceText.style.opacity = '1';
                }, (index * 100) + 150); // Additional delay for text
            }
        } else {
            // Hide with fade out
            row.style.transform = 'scale(0.95)';
            row.style.opacity = '0';
            setTimeout(() => {
                row.style.display = 'none';
            }, 300);

            if (serviceText && serviceText.classList.contains('service-text')) {
                serviceText.style.transform = 'scale(0.95)';
                serviceText.style.opacity = '0';
                setTimeout(() => {
                    serviceText.style.display = 'none';
                }, 300);
            }
        }
    });

    // Show/hide no results message with animation
    if (!hasVisibleServices && searchText !== '') {
        noResultsDiv.style.display = 'block';
        noResultsDiv.style.transform = 'scale(0.95)';
        noResultsDiv.style.opacity = '0';
        
        setTimeout(() => {
            noResultsDiv.style.transform = 'scale(1)';
            noResultsDiv.style.opacity = '1';
        }, 10);
    } else {
        noResultsDiv.style.transform = 'scale(0.95)';
        noResultsDiv.style.opacity = '0';
        setTimeout(() => {
            noResultsDiv.style.display = 'none';
        }, 300);
    }
}

// Add event listener when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('serviceSearch').addEventListener('input', searchServices);
});