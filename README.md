# Real Trust – Full Stack Landing Page & Admin Panel

A full-stack web application built as part of a Full Stack Development assignment.  
The project consists of a **responsive landing page** and an **admin panel** to manage projects, clients, contact form submissions, and newsletter subscriptions.

---

## 🚀 Features Overview

### Landing Page
- Responsive UI built with **HTML, CSS, Bootstrap**
- Dynamic content fetched from backend APIs
- Sections included:
  - **Our Projects** (fetched from backend)
  - **Happy Clients** (fetched from backend)
  - **Contact Form** (submits data to backend)
  - **Newsletter Subscription** (email stored in backend)

### Admin Panel
- Secure Django Admin interface
- Manage:
  - Projects (image, name, description)
  - Clients (image, name, description, designation)
  - Contact form submissions (view-only)
  - Newsletter subscribers (view-only)
- Image upload support
- Optional image cropping before save (bonus feature)

---

## 🛠 Tech Stack

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript (ES6)
- Django Templates

### Backend
- Python
- Django
- Django REST Framework
- Pillow (for image handling)

### Database
- SQLite (development)
- Easily extendable to PostgreSQL / MongoDB Atlas

---

## 📁 Project Structure

```

Landing_page_Harsh_Gehlot/
│
├── backend/
│   ├── core/               # Django project settings
│   ├── projects/           # Projects app
│   ├── clients/            # Clients app
│   ├── contacts/           # Contact form app
│   ├── newsletter/         # Newsletter subscription app
│   ├── media/              # Uploaded images
│   └── manage.py
│
├── frontend/
│   ├── templates/
│   │   └── index.html      # Main landing page
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css   # Custom styles
│   │   ├── js/
│   │   │   └── main.js     # API integration & form handling
│   │   └── images/         # SVG assets and images
│   └── README.md
│
└── README.md               # Project documentation

```

---

## 🎨 Frontend Structure

This directory contains the frontend assets for the **Real Trust landing page**.

### Directory Structure

```

frontend/
├── templates/
│   └── index.html          # Main landing page template
├── static/
│   ├── css/
│   │   └── style.css       # Custom styles
│   ├── js/
│   │   └── main.js         # JavaScript for API integration
│   └── images/             # SVG images and assets
│       ├── *.svg
└── README.md

````

---

## 📄 Files Description

### Templates
- **index.html**
  - Uses Django template tags
  - Renders all landing page sections
  - Loads static assets using `{% static %}`

### Static Files

#### CSS (`static/css/style.css`)
Includes:
- CSS variables for theming
- Navigation bar styles
- Hero section layout
- Project & client cards
- Forms and buttons
- Responsive breakpoints

#### JavaScript (`static/js/main.js`)
Handles:
- Fetching projects and clients from backend APIs
- Contact form submission
- Newsletter subscription
- Error handling and validations
- Safe DOM updates

#### Images (`static/images/`)
- SVG icons
- Decorative shapes
- Section illustrations
- All assets are optimized for performance

---

## 🔗 API Endpoints

The frontend communicates with the Django REST API:

| Method | Endpoint | Description |
|------|---------|------------|
| GET | `/api/projects/` | Fetch all projects |
| GET | `/api/clients/` | Fetch all clients |
| POST | `/api/contacts/` | Submit contact form |
| POST | `/api/newsletter/` | Subscribe email |

All APIs return JSON responses with proper status codes.

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/harshgehlot-code/Landing_page_Harsh_Gehlot.git
cd Landing_page_Harsh_Gehlot
````

### 2. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 3. Access Application

* Landing Page: `http://127.0.0.1:8000/`
* Admin Panel: `http://127.0.0.1:8000/admin/`

---

## 🌐 Deployment

* Backend deployed using platforms like **Render / Railway / AWS**
* Static & media files properly configured
* Repository is public and deployment-ready

---

## ✅ Evaluation Checklist

* ✔ Full-stack implementation
* ✔ Clean, modular code
* ✔ Backend-driven dynamic content
* ✔ Admin panel functionality
* ✔ Responsive UI
* ✔ Proper API integration

---

## 👨‍💻 Author

**Harsh Gehlot**
Computer Science Engineer | Full Stack & ML Enthusiast
GitHub: [https://github.com/harshgehlot-code](https://github.com/harshgehlot-code)

---

## 📌 Notes

* No framework-specific naming used in repository (as per instructions)
* Images are stored in `media/` after upload
* SVGs are preferred for performance
* Code is structured for scalability

---

```

---

### If you want next:
- I can **align screenshots with README**
- Add **API documentation**
- Improve **GitHub repo presentation**
- Review admin UX vs Flipr expectations

Just tell me.
```
