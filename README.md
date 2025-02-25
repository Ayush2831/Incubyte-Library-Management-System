# Library Management System

## Overview

The Library Management System is a simple application that allows users to manage books in a library. Users can add new books, borrow available books, return borrowed books, and view all available books in the library. This project follows Test-Driven Development (TDD) practices and adheres to SOLID principles of software design.

## Features

- **Add Books**: Add new books to the library with a unique identifier (ISBN), title, author, and publication year.
- **Borrow Books**: Borrow available books from the library, with checks for availability.
- **Return Books**: Return borrowed books, updating their availability.
- **View Available Books**: List all books currently available for borrowing.

## Technologies Used

- Python
- Unittest (for testing)

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd library_management_system

2. (Optional) Create a virtual environment and activate it:

    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install any necessary packages (if applicable):

    ```bash
    pip install -r requirements.txt  # If you have a requirements file


### Running the Tests

1. To run the tests for this project, execute:
    ```bash
    python -m unittest discover
