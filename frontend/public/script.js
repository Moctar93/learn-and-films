document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/tutorials')
        .then(response => response.json())
        .then(data => {
            const tutorialsContainer = document.querySelector('.content-row:nth-of-type(1) .content-grid');
            tutorialsContainer.innerHTML = data.map(tutorial => `
                <div class="content-item">
                    <img src="https://via.placeholder.com/150" alt="${tutorial.title}">
                    <p>${tutorial.title}</p>
                </div>
            `).join('');
        });

    fetch('/api/movies')
        .then(response => response.json())
        .then(data => {
            const moviesContainer = document.querySelector('.content-row:nth-of-type(2) .content-grid');
            moviesContainer.innerHTML = data.map(movie => `
                <div class="content-item">
                    <img src="https://via.placeholder.com/150" alt="${movie.title}">
                    <p>${movie.title}</p>
                </div>
            `).join('');
        });
});

