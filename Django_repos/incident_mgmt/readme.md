# 🚨 Incident Management System - DRF Project

A RESTful API for managing incidents within an organization. Built using Django REST Framework with token-based authentication and custom user support.

---

## 📦 Features

- ✅ User registration and login
- 🔐 Token-based authentication
- 🧑‍💼 Custom user model with extended fields (address, pincode, etc.) where user have to enter only pincode to save           corresponding city and country autocalculated by use of geopy library.
- 📝 Create, view, update incidents
- 🚫 Prevent edits if status is "Closed"
- 🔍 Filter incidents by user
- 📅 Auto-generated `incident_id` and `reported_at` fields

---

## 🛠 Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default) / MySQL (optional)
- **Authentication**: Token-based (via `rest_framework.authtoken`)

---

## 🚀 Getting Started

### 1. Extract the zip file to get project folder "incident_mgmt"
cd incident_mgmt

### 2. Set Up Virtual Environment
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

### 5. Create Superuser (Optional)
python manage.py createsuperuser

### 6. Run the Server
python manage.py runserver


🔑 API Authentication

### Obtain a token via login:

    POST /api/accounts/login/

    Input json
    {
    "username": "your_username",
    "password": "your_password"
    }

    Response:
    {
    "token": "your_token"
}

### Use the token in headers:
    Authorization: Token your_token



🧪 API Endpoints
    Method	        Endpoint	                               Description	                                   Auth Required
    POST	    /api/accounts/register/	                    Register new user	                                    ❌
    POST	    /api/accounts/login/	                    Login and get token	                                    ❌
    GET	        /api/incidents/	                            List user’s incidents	                                ✅
    POST	    /api/incidents/	                            Create a new incident	                                ✅
    PUT	        /api/incidents/<id>/	                    Update an incident	                                    ✅
    DELETE	    /api/incidents/<id>/	                    Delete an incident	                                    ✅
    POST	    /api/accounts/forgot-password/	            Request password reset link	                            ❌
    POST	    /api/accounts/reset-password/?uid=&token=	Reset password using token	                            ❌

