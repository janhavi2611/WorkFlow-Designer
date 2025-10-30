# ✅ To-Do List Web Application (Django)

A fully functional **To-Do List Web Application** built using the **Django Framework**, that allows users efficiently organize and manage their daily tasks.  
It features **User Authentication**, **Task Prioritization**, **Task Categorization**, **Progress Tracking**, and **Admin Controls**, offering both functionality and an elegant UI.  

Developed as part of the **Python Mini Project** for academic evaluation.

---

| Name | Contribution |
|------|---------------|
| **Diksha More** | Authentication, documentation, UI/UX |
| **Janhavi Jadhav** | Backend |
| **Shravanee Kumbhar** | Frontend |
| **Sejal Wable** | Database |

---

## 💡 Project Overview

The **To-Do List Web App** allows users to manage daily activities efficiently by adding, categorizing, prioritizing, and tracking their tasks.  

Each registered user has a **personal dashboard** to view and manage their own tasks securely.    

Users can **sign up, log in, and maintain separate task lists** securely.

---

## ⚙️ Features

### 👤 **User Management**
- User can **Signup, Login, Logout**
- Passwords stored securely with Django’s authentication system
- Admin can **add, edit, and delete users**
- Each user has their **own isolated task list**

---

### 📝 **Task Management**
#### ➕ Core Features
- Add, edit, and delete tasks  
- Mark tasks as **completed** or **pending**  
- Set **due dates**, **categories**, and **priority levels**  

#### 🎯 **Task Prioritization**
- Assign **priority levels**: High, Medium, or Low  
- Sorting and filtering available by priority or category  

#### 🗂️ **Task Segregation & Filtering**
- Tasks filtered by **category**, **status**, or **priority**
- View **pending**, **completed**, and **overdue** tasks easily  
- Search bar for quick lookup of tasks  

#### 📈 **Task Progress Tracker**
- Real-time **progress bar** showing completion percentage  

---

### 🎨 **User Interface & Rendering**
- Built using **HTML, CSS, and Bootstrap** for a modern and responsive look  
- **Django Template Rendering** dynamically loads data based on the user session  
- Soft pastel UI theme for better readability and user comfort  
- Intuitive icons for edit, delete, and complete actions  

---

## 🧱 Architecture & Database Schema

### 🏗️ **Architecture**
The project follows Django’s **Model–View–Template (MVT)** structure:


**Flow:**
1. User interacts with templates (UI).  
2. Views handle business logic and user requests.  
3. Models interact with the database (SQLite).  
4. Rendered templates display updated data back to the user.

---

### 🗄️ **Database Schema**

| Table | Key Fields | Description |
|--------|-------------|-------------|
| **User** | id, username, password, email | Stores user authentication data |
| **Task** | id, user_id (ForeignKey), title, description, due_date, status, priority, category | Stores individual tasks linked to users |

**Relationships:**
- One-to-Many: A single user can have multiple tasks.
- Foreign Key: `user_id` connects each task to its respective user.

---

## 🎨 Design Decisions

1. **Framework Choice:**  
   Django was chosen for its built-in authentication, ORM, and scalability.

2. **Database:**  
   SQLite was selected for simplicity and lightweight usage during development.

3. **UI Design:**  
   - Implemented a clean and minimal design using **Bootstrap**.  
   - Prioritized readability and responsiveness across devices.  
   - Added subtle shadows and gradients for a professional look.

4. **Task Prioritization & Categorization:**  
   - Added dropdown menus for **category**, **status**, and **priority** filters.  
   - Integrated icons and badges for better visual feedback.  


---

## 🧠 Concepts Learned

During the development of this project, our team learned and implemented the following core concepts:

### 🔹 **Python & Django Concepts**
- Understanding Django’s **MVT (Model–View–Template)** architecture.  
- Working with **Django ORM** for database operations.  
- Implementing **authentication & authorization** systems.  
- Managing **forms**, **URL routing**, and **views** in Django.  

### 🔹 **Team Collaboration**
- Using **Git & GitHub** for version control.  
- Collaborative coding, conflict resolution, and code reviews.  
- Documenting features and maintaining consistency across files.

---

  
## 🧠 Challenges Faced

1. **User-specific Task Handling:**  
   Ensuring each user sees only their own tasks required careful query filtering using Django ORM.

2. **Dynamic Filtering and Sorting:**  
   Implementing combined filters for category, status, and priority while maintaining performance.


3. **Responsive UI Issues:**  
   Adjusting layouts for mobile screens using CSS and Bootstrap grid system.


---

## 🚀 Future Improvements

- 📅 **Add Task Deadlines & Notifications:** Email or in-app reminders.   
- 🔔 **Task Alerts:** Add pop-up or email alerts for due tasks.  
- 🗓️ **Calendar Integration:** Visual calendar view for all tasks.  
- 🌙 **Dark Mode:** Toggle between light and dark themes.  
- 🔍 **Advanced Filters:** Search by date range or keyword tags.
  

---

## 📸 Screenshots (App Flow)

### 🏠 Home / Dashboard
<img width="1864" height="884" alt="Screenshot 2025-10-30 210124" src="https://github.com/user-attachments/assets/00c30c4a-c41b-48bd-ae0d-b20ed0171638" />


### ➕ Add New Task
<img width="1882" height="870" alt="Screenshot 2025-10-30 210201" src="https://github.com/user-attachments/assets/a80c71b4-3b97-4ab3-aca0-00652f728b99" />


---



