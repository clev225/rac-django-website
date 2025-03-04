document.addEventListener('DOMContentLoaded', function() {
    // Load the footer component
    (function() {
        var xhrFooter = new XMLHttpRequest();
        xhrFooter.open('GET', 'components/footer.html', true);
        xhrFooter.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                document.getElementById('footer-placeholder').innerHTML = this.responseText;
            }
        };
        xhrFooter.send();
    })();
});