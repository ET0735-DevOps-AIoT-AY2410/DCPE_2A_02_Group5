// books.js
const books = [
    {
        title: "To Kill a Mockingbird",
        author: "Harper Lee",
        cover: "data/book_covers/Mockingbird.jpg", // Adjust path as needed
        description: "...", // Add the book's description
        genres: ["Southern Gothic", "Legal Drama"],
        availability: ["Main Branch", "North Branch"]
    },
    {
        title: "The Hitchhiker's Guide to the Galaxy",
        author: "Douglas Adams",
        cover: "data/book_covers/Hitchhiker.jpg", // Adjust path as needed
        description: "...", // Add the book's description
        genres: ["Science Fiction", "Humor"],
        availability: ["Main Branch", "South Branch", "East Branch"]
    },
    {
        title: "The Great Gatsby",
        author: "F. Scott Fitzgerald",
        cover: "data/book_covers/Gatsby.jpg",  // Adjust path as needed
        description: "...", // Add the book's description
        genres: ["Tragedy"],
        availability: ["Main Branch", "East Branch", "West Branch"]
    }
];

export default books;
