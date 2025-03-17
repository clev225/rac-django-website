document.addEventListener('DOMContentLoaded', function() {
    // Load the footer component
    (function() {
        var xhrFooter = new XMLHttpRequest();
        xhrFooter.open('GET', 'components/footer.html', true);
        xhrFooter.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                var footerPlaceholder = document.getElementById('footer-placeholder');
                footerPlaceholder.innerHTML = this.responseText;

                // Ensure footer takes full width
                var footer = footerPlaceholder.querySelector('footer');
                if (footer) {
                    footer.classList.add('w-100');
                    footer.style.marginLeft = '0';
                    footer.style.marginRight = '0';
                    footer.style.maxWidth = '100%';
                }
            }
        };
        xhrFooter.send();
    })();
});
