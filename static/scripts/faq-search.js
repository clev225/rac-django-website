function searchFAQs() {
    const searchInput = document.getElementById('faqSearch');
    const searchText = searchInput.value.toLowerCase();
    const faqItems = document.querySelectorAll('.faq-item');
    const noResultsDiv = document.getElementById('noFAQResults');
    let hasVisibleFAQs = false;

    faqItems.forEach((item, index) => {
        const question = item.querySelector('.faq-question').textContent.toLowerCase();
        const answer = item.querySelector('.faq-answer').textContent.toLowerCase();
        const isVisible = question.includes(searchText) || answer.includes(searchText);
        
        if (isVisible) {
            hasVisibleFAQs = true;
            // Show with popup animation
            item.style.transition = 'all 0.3s ease-out';
            item.style.transform = 'scale(0.95)';
            item.style.opacity = '0';
            item.style.display = 'block';
            
            setTimeout(() => {
                item.style.transform = 'scale(1)';
                item.style.opacity = '1';
            }, index * 100); // Staggered delay based on index
        } else {
            // Hide with fade out
            item.style.transform = 'scale(0.95)';
            item.style.opacity = '0';
            setTimeout(() => {
                item.style.display = 'none';
            }, 300);
        }
    });

    // Show/hide no results message with animation
    if (!hasVisibleFAQs && searchText !== '') {
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

// Add event listeners when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('faqSearch');
    const searchButton = document.querySelector('.search-button');
    
    searchInput.addEventListener('input', searchFAQs);
    searchButton.addEventListener('click', searchFAQs);
});