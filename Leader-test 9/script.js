class Book {
    constructor(title, author) {
        this.title = title;
        this.author = author;
        this.read = false;
    }
}

const books = [
    new Book('Don Quixote', 'Miguel de Cervantes'),
    new Book('Alice\'s Adventures in Wonderland', 'Lewis Carroll'),
    new Book('The Adventures of Huckleberry Finn', 'Mark Twain')
];

const booksContainer = document.getElementById('books');
const libraryContainer = document.getElementById('library');
let library = JSON.parse(localStorage.getItem("library")) || [];

function renderBooks() {
    booksContainer.innerHTML = "";
    books.forEach((book, index) => {
        const bookDiv = document.createElement("div");
        bookDiv.classList.add("book");
        bookDiv.innerHTML = `<h3>${book.title}</h3><p>${book.author}</p>`;

        const addButton = document.createElement("button");
        addButton.textContent = "Add to Library";
        addButton.addEventListener("click", () => addToLibrary(index));

        bookDiv.appendChild(addButton);
        booksContainer.appendChild(bookDiv);
    });
}

function renderLibrary() {
    libraryContainer.innerHTML = "";
    library.forEach((book, index) => {
        const bookDiv = document.createElement("div");
        bookDiv.classList.add("book");
        if (book.read) bookDiv.classList.add('read');

        bookDiv.innerHTML = `<h3>${book.title}</h3><p>${book.author}</p>`;

        const toggleButton = document.createElement("button");
        toggleButton.textContent = book.read ? "Unread" : "Read";
        toggleButton.classList.add("toggle");
        toggleButton.addEventListener("click", () => toggleRead(index));

        const removeButton = document.createElement("button");
        removeButton.textContent = "Remove";
        removeButton.classList.add("remove");
        removeButton.addEventListener("click", () => removeFromLibrary(index));

        bookDiv.appendChild(toggleButton);
        bookDiv.appendChild(removeButton);

        libraryContainer.appendChild(bookDiv);
    });
    localStorage.setItem("library", JSON.stringify(library));
}

function addToLibrary(index) {
    library.push(books[index]);
    renderLibrary();
}

function toggleRead(index) {
    library[index].read = !library[index].read;
    renderLibrary();
}

function removeFromLibrary(index) {
    library.splice(index, 1);
    renderLibrary();
}

function showSection(section) {
    document.getElementById("books").classList.remove("active");
    document.getElementById("library").classList.remove("active");
    document.getElementById(section).classList.add("active");
}


const addBookForm = document.getElementById('addBookForm');
addBookForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const newBookTitle = document.getElementById('newBookTitle').value;
    const newBookAuthor = document.getElementById('newBookAuthor').value;

    const newBook = new Book(newBookTitle, newBookAuthor);
    books.push(newBook);
    renderBooks();
    document.getElementById('newBookTitle').value = ''; // Reset the input fields
    document.getElementById('newBookAuthor').value = '';
});


renderBooks();
renderLibrary();
