// browse.js
import books from './books.js';

//Book Grid const
const bookGrid = document.querySelector('.book-grid');
const bookDetailModal = document.getElementById('book-detail');
const closeButton = document.querySelector('.close-button');

//Filter const
const genreFilter = document.getElementById('genreFilter');
const authorFilter = document.getElementById('authorFilter');
const availabilityFilter = document.getElementById('availabilityFilter');



// Function to display books in the grid
function displayBooks(books) {
    bookGrid.innerHTML = ''; // Clear the grid
    books.forEach(book => {
        const bookItem = document.createElement('div');
        bookItem.classList.add('book-item');
        bookItem.innerHTML = `
            <img class="book-cover" src="${book.cover}" alt="${book.title}">
            <div class="book-details">
                <h3>${book.title}</h3>
                <p>By ${book.author}</p>
                <p hidden>${book.bookId}</p>
            </div>
        `;


        // Event listener to open the modal
        bookItem.addEventListener('click', () => {
            displayBookDetail(book);
        });

        bookGrid.appendChild(bookItem);
    });
}


// Function to display book details in the modal
function displayBookDetail(book) {
    document.getElementById('detail-title').textContent = book.title;
    document.getElementById('detail-bookId').textContent = book.bookId;
    document.getElementById('detail-cover').src = book.cover;
    document.getElementById('detail-author').textContent = "By " + book.author;
    document.getElementById('detail-description').textContent = book.description;
     
    bookDetailModal.style.display = 'block';
}

function populateFilterOptions() {
    const genres = new Set();
    const availabilities = new Set();

    books.forEach(book => {
        book.genres.forEach(genre => genres.add(genre));
        
    });

    genres.forEach(genre => {
        const option = document.createElement('option');
        option.value = genre;
        option.text = genre;
        genreFilter.add(option);
    });

}


// Filter books based on selected criteria
function filterBooks() {
    const selectedGenre = genreFilter.value;
    const selectedAuthor = authorFilter.value.toLowerCase();

    const filteredBooks = books.filter(book => {
        const matchesGenre = selectedGenre === '' || book.genres.includes(selectedGenre);
        const matchesAuthor = selectedAuthor === '' || book.author.toLowerCase().includes(selectedAuthor);
        return matchesGenre && matchesAuthor;
    });

    displayBooks(filteredBooks);
}


// Event listener for closing the modal
closeButton.addEventListener('click', () => {
    bookDetailModal.style.display = 'none';
});

// Event listeners for filter changes
genreFilter.addEventListener('change', filterBooks);
authorFilter.addEventListener('input', filterBooks); // Filter as the user types


// Initial display of books once the DOM content is loaded
document.addEventListener('DOMContentLoaded', () => {
    displayBooks(books);
    populateFilterOptions();
});
