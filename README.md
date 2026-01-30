# BackendDeveloperHub FastAPI 🚀

This is a beginner-friendly **FastAPI starter project** created under
**BackendDeveloperHub** to help developers learn backend development
by building real-world APIs.

---

## 🔧 Tech Stack
- **Language:** Python
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Database:** SQLite (initially)

---

## 📁 Project Structure
backenddeveloperhub-fastapi/ │ ├── app/ │   ├── main.py │   ├── config.py │   ├── database.py │   │ │   ├── routes/ │   │   └── health.py │   │ │   ├── schemas/ │   │   └── health.py │   │ │   └── init.py │ ├── requirements.txt ├── README.md └── .gitignore

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/BackendDeveloperHub/backenddeveloperhub-fastapi.git
cd backenddeveloperhub-fastapi


Create Virtual Environment:-

python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows



Install Dependencies:-

pip install -r requirements.txt

4️⃣ Run the Server:-


uvicorn app.main:app --reload



