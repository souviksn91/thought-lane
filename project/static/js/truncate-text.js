// function to truncate text after a certain number of words
function truncateText(selector, wordLimit) {
    const elements = document.querySelectorAll(selector);
    elements.forEach(element => {
        const words = element.textContent.split(' ');
        if (words.length > wordLimit) {
            element.textContent = words.slice(0, wordLimit).join(' ') + '...';
        }
    });
}

// call the function to truncate text after 30 words
truncateText('.truncate-text', 30);

// call the function to truncate text after 14 words
truncateText('.truncate-text-card', 14);

// // call the function to truncate text after 20 words
// truncateText('.truncate-title-card', 20);