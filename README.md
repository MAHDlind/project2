# Project2

## 📌 Overview
**Project2** is a Django-based web application designed to [briefly describe the purpose or functionality of the project].  
The main objective of this project is to [state the goal, e.g., manage blog posts, user profiles, and handle contact forms].  

---

## ✨ Features
- 🔐 User authentication and profile management  
- 📝 Create and manage posts with categories  
- 📬 Contact form for user messages  
- 📢 Newsletter subscription system  
- ⚙️ Admin panel with Django’s built-in management tools  

---

## 🚀 Getting Started

### ✅ Prerequisites
Make sure you have the following installed:
- Python **3.x**
- Django (see `requirements.txt`)
- Other dependencies (installed via `pip`)

### ⚡ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/project2.git
   cd project2
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## 📊 Database Schema

This project uses **Django ORM** with the following core models:

### 🔐 Authentication & Permissions
- **User (AbstractUser)** – Manages authentication and user details  
- **Group & Permission** – Role-based access control  
- **LogEntry, ContentType, Session** – Internal Django utilities for logging and session management  

### 👤 Profile
- **Profile**  
  - `OneToOne` relation with `User`  
  - Fields: `profile_image`  

### 📝 Post & Category
- **Post**  
  - `ForeignKey` to `User` (author)  
  - `ForeignKey` to `Category`  
  - Fields: `title/subject`, `text`, `image`, `published_date`, `updated_at`, `published_status`  

- **Category**  
  - Fields: `name`  

### 📬 Contact & Newsletter
- **Contact**  
  - Fields: `name`, `email`, `subject`, `message`, `sent_at`  

- **NewsLetterForm**  
  - Fields: `email`  

### Schema Diagram
![Database Schema](myapp_models.png)

---

## 🛠️ Usage
- Users can sign up, log in, and update their profile  
- Admins can manage posts, categories, and users via the Django admin panel  
- Visitors can send messages using the contact form  
- Users can subscribe to the newsletter  

---

## 📬 Contact
- 📧 Email: [qwrwfwtsewqr@gmail.com](mailto:qwrwfwtsewqr@gmail.com)  
- 🐙 GitHub: [MAHDlind](https://github.com/MAHDlind)  
- 💼 LinkedIn: [Mahdi Hosseinkhani](https://www.linkedin.com/in/mahdi-hosseinkhani-4551202a4)  
