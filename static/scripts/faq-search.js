function searchFAQs() {
    const searchInput = document.getElementById('faqSearch');
    const searchText = searchInput.value.trim().toLowerCase(); // Add trim() to handle whitespace
    const faqItems = document.querySelectorAll('.faq-item');
    const noResultsDiv = document.getElementById('noFAQResults');
    let hasVisibleFAQs = false;

    // If search is empty, show all items without highlights
    if (!searchText) {
        faqItems.forEach(item => {
            const question = item.querySelector('.faq-question');
            const answer = item.querySelector('.faq-answer');
            
            // Reset to original text if stored
            if (question.dataset.originalText) {
                question.innerHTML = question.dataset.originalText;
                answer.innerHTML = answer.dataset.originalText;
            }
            
            item.style.display = 'block';
            item.style.opacity = '1';
        });
        noResultsDiv.style.display = 'none';
        return;
    }

    // Rest of the search logic for non-empty search
    faqItems.forEach((item, index) => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        
        // Store original text if not already stored
        if (!question.dataset.originalText) {
            question.dataset.originalText = question.innerHTML;
            answer.dataset.originalText = answer.innerHTML;
        }

        // Reset to original text
        question.innerHTML = question.dataset.originalText;
        answer.innerHTML = answer.dataset.originalText;

        const questionText = question.textContent.toLowerCase();
        const answerText = answer.textContent.toLowerCase();
        const isVisible = questionText.includes(searchText) || answerText.includes(searchText);

        if (isVisible) {
            hasVisibleFAQs = true;
            const regex = new RegExp(`(${searchText})`, 'gi');
            question.innerHTML = question.innerHTML.replace(regex, '<span class="highlight">$1</span>');
            answer.innerHTML = answer.innerHTML.replace(regex, '<span class="highlight">$1</span>');
            item.style.display = 'block';
            item.style.opacity = '1';
        } else {
            item.style.display = 'none';
            item.style.opacity = '0';
        }
    });

    noResultsDiv.style.display = hasVisibleFAQs ? 'none' : 'block';
}

// Add event listeners when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('faqSearch');
    const searchButton = document.querySelector('.search-button');
    
    searchInput.addEventListener('input', searchFAQs);
    searchButton.addEventListener('click', searchFAQs);
});