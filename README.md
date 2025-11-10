# 🚗 Car Dealership REST API

**First ever Django REST project!**  
This project demonstrates my foundational skills in building RESTful APIs with Django REST Framework. It implements a simple car dealership management system with core functionality for managing employees, cars, and users. No frontend yet—focus is fully on backend logic and API design.

---

## 🔑 Core Features

- 🛠 **Django REST Framework backend**
- 👨‍💼 **Employee management** (Create, Read, Update, Delete, Search)
- 🚗 **Car management** with relational linking to owners
- 🧍‍♂️ **User registration and profile management**
- 🔐 **Token-based authentication** with DRF `TokenAuthentication`
- 📊 **Filtering, searching, and pagination support**
- ✅ **Fully modular app structure** (`core`, `car`, `employee`, `new_user`)

---

## 🧩 Project Structure

car-dealership/
│
├─ core/ # General endpoints (hello world, calculator)
├─ car/ # Car and Person API endpoints (ModelViewSets)
├─ employee/ # Employee CRUD endpoints
├─ new_user/ # User registration and profile endpoints
├─ djangorest/ # Django project root
└─ requirements.txt 


---

## 👨‍💻 Author

**Alireza Golshan**  
💼 Computer Science Student | Django & REST Developer  
🐍 Passionate about backend logic & API development  
🔗 [GitHub](https://github.com/alirzglshn) • [LinkedIn](https://www.linkedin.com/in/alirzglshn/)

---

## 🧭 Future Improvements

- Add Swagger/OpenAPI documentation  
- Implement JWT authentication for enhanced security  
- Deploy project with Docker  
- Add a React frontend for fullstack integration

---

## 🚀 How to Run

Clone the repo 

```bash
git clone https://github.com/alirzglshn/car-dealership.git
cd car-dealership


Setup virtual environment

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Configure your database
Update djangorest/settings.py with your MySQL credentials.

Run migrations

python manage.py makemigrations
python manage.py migrate


Create a superuser

python manage.py createsuperuser


Run the server

python manage.py runserver
