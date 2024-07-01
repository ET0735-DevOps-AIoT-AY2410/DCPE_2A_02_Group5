// script.js
import books from './data/books.js';
//import users from './data/users.js';

const bookGrid = document.querySelector('.book-grid');
const bookDetailModal = document.getElementById('book-detail');
const closeButton = document.querySelector('.close-button');

const genreFilter = document.getElementById('genreFilter');
const authorFilter = document.getElementById('authorFilter');
const availabilityFilter = document.getElementById('availabilityFilter');

const loginForm = document.getElementById('loginForm');
const loginMessage = document.getElementById('login-message');
const accountInfo = document.getElementById('account-info');
const currentLoans = document.getElementById('current-loans');
const reservationHistory = document.getElementById('reservation-history');

// Hardcoded user accounts (for demonstration purposes)
const users = {
    'user': {
        username: 'user',
        password: 'password',
        profile: {
            name: 'John Doe',
            email: 'john.doe@example.com',
        },
        loans: ['Book 1', 'Book 2'],
        reservations: ['Book 3', 'Book 4']
    }
};

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
    document.getElementById('detail-cover').src = book.cover;
    document.getElementById('detail-author').textContent = "By " + book.author;
    document.getElementById('detail-description').textContent = book.description;
    document.getElementById('detail-availability').textContent = "Available at: " + book.availability.join(', ');
    
    bookDetailModal.style.display = 'block';
}

function populateFilterOptions() {
    const genres = new Set();
    const availabilities = new Set();

    books.forEach(book => {
        book.genres.forEach(genre => genres.add(genre));
        book.availability.forEach(availability => availabilities.add(availability));
    });

    genres.forEach(genre => {
        const option = document.createElement('option');
        option.value = genre;
        option.text = genre;
        genreFilter.add(option);
    });

    availabilities.forEach(availability => {
        const option = document.createElement('option');
        option.value = availability;
        option.text = availability;
        availabilityFilter.add(option);
    });
}

// Filter books based on selected criteria
function filterBooks() {
    const selectedGenre = genreFilter.value;
    const selectedAuthor = authorFilter.value.toLowerCase();
    const selectedAvailability = availabilityFilter.value;

    const filteredBooks = books.filter(book => {
        const matchesGenre = selectedGenre === '' || book.genres.includes(selectedGenre);
        const matchesAuthor = selectedAuthor === '' || book.author.toLowerCase().includes(selectedAuthor);
        const matchesAvailability = selectedAvailability === '' || book.availability.includes(selectedAvailability);
        return matchesGenre && matchesAuthor && matchesAvailability;
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
availabilityFilter.addEventListener('change', filterBooks);

// Initial display of books once the DOM content is loaded
document.addEventListener('DOMContentLoaded', () => {
    displayBooks(books);
    populateFilterOptions();
});

// Handle login form submission
if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const username = e.target.username.value;
        const password = e.target.password.value;

        const user = users[username];

        // Simple authentication logic (for demonstration purposes)
        if (user && user.password === password) {
            loginMessage.textContent = 'Login successful!';
            loginForm.style.display = 'none';
            accountInfo.style.display = 'block';
            currentLoans.style.display = 'block';
            reservationHistory.style.display = 'block';

            // Display user profile information
            accountInfo.innerHTML = `<h3>Profile</h3><p>Name: ${user.profile.name}</p><p>Email: ${user.profile.email}</p>`;
            
            // Display current loans
            currentLoans.innerHTML = `<h3>Current Loans</h3><ul>${user.loans.map(loan => `<li>${loan}</li>`).join('')}</ul>`;

            // Display reservation history
            reservationHistory.innerHTML = `<h3>Reservation History</h3><ul>${user.reservations.map(reservation => `<li>${reservation}</li>`).join('')}</ul>`;

            // Redirect to dashboard
            window.location.href = 'dashboard.html';
        } else {
            loginMessage.textContent = 'Invalid username or password. Please try again.';
        }
    });
}

// Handle dashboard display
document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname.endsWith('dashboard.html')) {
        const username = 'user'; // Replace this with logic to get the logged-in user
        const user = users[username];

        if (user) {
            document.getElementById('username').textContent = user.profile.name;

            // Display current loans
            document.getElementById('loans-list').innerHTML = user.loans.map(loan => `<li>${loan}</li>`).join('');

            // Display outstanding fines
            document.getElementById('fines-amount').textContent = `Outstanding Fines: $${user.fines.toFixed(2)}`;
        }
    }
});

// Handle account form submission and redirect
document.addEventListener('DOMContentLoaded', () => {
    // Handle account form submission
    const accountForm = document.getElementById('accountForm');
    if (accountForm) {
        accountForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // Handle the form submission logic here
            // For example, you might want to collect form data and validate it
            const formData = new FormData(accountForm);
            const accountData = {
                username: formData.get('username'),
                email: formData.get('email'),
                // Add other form fields as necessary
            };

            // Assume the form submission is successful
            // Redirect to the dashboard
            window.location.href = 'dashboard.html';
        });
    }
});
