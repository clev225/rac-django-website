function searchServices() {
    const searchInput = document.getElementById('serviceSearch');
    const searchText = searchInput.value.trim().toLowerCase();
    const serviceRows = document.querySelectorAll('.service-row');
    const noResultsDiv = document.getElementById('noResults');
    let hasVisibleServices = false;

    // If search is empty, show all items without highlights
    if (!searchText) {
        serviceRows.forEach(row => {
            row.style.display = 'block';
            row.style.opacity = '1';
            
            // Reset all highlights
            const title = row.querySelector('.service-title');
            const listItems = row.querySelectorAll('.service-text li');
            
            if (title.dataset.originalText) {
                title.innerHTML = title.dataset.originalText;
            }
            
            listItems.forEach(item => {
                if (item.dataset.originalText) {
                    item.innerHTML = item.dataset.originalText;
                }
            });
        });
        noResultsDiv.style.display = 'none';
        return;
    }

    // Search logic for non-empty search
    serviceRows.forEach((row) => {
        const title = row.querySelector('.service-title');
        const listItems = row.querySelectorAll('.service-text li');
        
        // Store original text if not already stored
        if (!title.dataset.originalText) {
            title.dataset.originalText = title.innerHTML;
        }
        listItems.forEach(item => {
            if (!item.dataset.originalText) {
                item.dataset.originalText = item.innerHTML;
            }
        });

        // Reset to original text
        title.innerHTML = title.dataset.originalText;
        listItems.forEach(item => {
            item.innerHTML = item.dataset.originalText;
        });

        const titleText = title.textContent.toLowerCase();
        const listTexts = Array.from(listItems).map(item => item.textContent.toLowerCase());
        
        // Check if search text matches title or any list item
        const isVisible = titleText.includes(searchText) || 
                         listTexts.some(text => text.includes(searchText));

        if (isVisible) {
            hasVisibleServices = true;
            const regex = new RegExp(`(${searchText})`, 'gi');
            
            // Highlight matching text in title
            if (titleText.includes(searchText)) {
                title.innerHTML = title.innerHTML.replace(regex, '<span class="highlight">$1</span>');
            }
            
            // Highlight matching text in list items
            listItems.forEach(item => {
                if (item.textContent.toLowerCase().includes(searchText)) {
                    item.innerHTML = item.innerHTML.replace(regex, '<span class="highlight">$1</span>');
                }
            });
            
            row.style.display = 'block';
            row.style.opacity = '1';
        } else {
            row.style.display = 'none';
            row.style.opacity = '0';
        }
    });

    noResultsDiv.style.display = hasVisibleServices ? 'none' : 'block';
}

// Add event listeners when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('serviceSearch');
    const searchButton = document.querySelector('.search-button');
    
    searchInput.addEventListener('input', searchServices);
    searchButton.addEventListener('click', searchServices);
});