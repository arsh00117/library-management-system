# 📚 LBR MG - Library Management System

> A secure and robust **console-based Library Management System** built using **Python**, **SQLite**, and **Object-Oriented Programming (OOP)** principles.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge\&logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge\&logo=sqlite)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-success?style=for-the-badge)
![OOP](https://img.shields.io/badge/OOP-Implemented-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![CLI](https://img.shields.io/badge/Application-CLI-lightgrey?style=for-the-badge)
![Made By](https://img.shields.io/badge/Made%20By-Arshdeep%20Singh-red?style=for-the-badge)

---

# 📖 Overview

The **LBR MG - Library Management System** is a command-line application designed to efficiently manage library records using **SQLite** for persistent storage.

The project demonstrates modern Python programming concepts while providing essential library operations such as adding, searching, issuing, and returning books.

The project focuses on:

* Object-Oriented Programming (OOP)
* SQLite Database Integration
* Exception Handling
* Input Validation
* Clean & Modular Code

---

# ✨ Features

✅ Add New Books

✅ View All Books

✅ Search Books by Title

✅ Issue Books

✅ Return Books

✅ Real-Time Library Statistics

✅ SQLite Database Storage

✅ Input Validation

✅ Exception Handling

---

# 🛠 Technologies Used

* Python 3
* SQLite3
* Object-Oriented Programming (OOP)
* SQL
* Exception Handling
* Command Line Interface (CLI)

---

# 📂 Project Structure

```text
LBR-MG/
│
├── main.py
├── database.db        # Automatically created
├── README.md
```

---

# 🔄 Workflow

```text
                  +----------------------+
                  |     Start Program    |
                  +----------+-----------+
                             |
                             ▼
                  +----------------------+
                  |     Main Menu        |
                  +----------+-----------+
                             |
      +----------+-----------+------------+-----------+
      |          |           |            |           |
      ▼          ▼           ▼            ▼           ▼
 Add Book   Show Books   Search Book  Issue Book  Return Book
      |          |           |            |           |
      +----------+-----------+------------+-----------+
                             |
                             ▼
                  +----------------------+
                  |   Update Database    |
                  +----------+-----------+
                             |
                             ▼
                     View Statistics
                             |
                             ▼
                           Exit
```

---

## 📊 Application Modules

* ✅ Book Management
* ✅ Add Book
* ✅ Search Book
* ✅ Issue Book
* ✅ Return Book
* ✅ Library Statistics
* ✅ SQLite Database
* ✅ Exception Handling

---

# 🗄️ Database Schema

| Column      | Type                              |
| ----------- | --------------------------------- |
| BOOK_ID     | INTEGER PRIMARY KEY AUTOINCREMENT |
| BOOK_TITLE  | TEXT                              |
| BOOK_AUTHOR | TEXT                              |
| STATUS      | INTEGER                           |

### Status Codes

| Value | Meaning   |
| ----- | --------- |
| 0     | Available |
| 1     | Issued    |

---

# 💻 Sample Menu

```text
====== LIBRARY MANAGEMENT SYSTEM ======

1. Show all books
2. Add book
3. Issue book
4. Return book
5. Search book
6. Statistics
7. Exit
```

---

# 📈 Statistics

The application provides:

* 📚 Total Books
* 📕 Issued Books
* 📗 Available Books

---

# 🚀 Future Improvements

* User Authentication
* Student/Borrower Management
* Due Date Tracking
* Fine Calculation
* Book Categories
* Update & Delete Books
* Transaction History
* Export Records to CSV/Excel
* GUI Version using Tkinter or PyQt
* Web Version using Flask or Django

---

# 📚 Concepts Covered

* Classes & Objects
* Constructors
* SQLite Database
* SQL CRUD Operations
* Methods
* Loops
* Conditional Statements
* Exception Handling
* Input Validation
* Modular Programming

---

# 👨‍💻 Author

## **Arshdeep Singh (ARSH)**

Python Developer | Software Engineering Student

> *"Learning by Building Real Projects."*

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub!

---

<div align="center">

### Made with ❤️ by **Arshdeep Singh**

</div>
