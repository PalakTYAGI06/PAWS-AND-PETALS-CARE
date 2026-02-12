# PAWS AND PETAL CARE WEBSITE

Simple Django website for pet care and booking functionality.

## Project layout

- `PAWS AND PETAL CARE WEBSITE/` — Django project and apps (`core`, `booking`).
- `templates/` — project-level templates (home, service, register, etc.).
- `static/` — CSS/JS used by templates.
- `db.sqlite3` — SQLite database (development).

## Requirements

- Python 3.10+ (this project used 3.13 in the environment)
- Virtual environment with packages in `requirement.txt` (already generated).

## Quick start (development)

1. Create and activate a venv (if you don't have one):

```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirement.txt
```

3. Apply migrations and create a superuser:

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser.

## Media & Static files

- `MEDIA_ROOT` is configured to `media/` in settings; uploaded files will be stored there.
- Static files (CSS/JS) live in the `static/` folder; `STATICFILES_DIRS` is set.

## Configuration notes

- Sensitive values in `config/settings.py` (e.g. `SECRET_KEY`, email password) should be moved to environment variables for production.
- `DEBUG = True` in settings — set to `False` for production.
- Templates DIR was adjusted to `BASE_DIR / 'templates'` so Django finds project templates.

## Troubleshooting

- If you see `TemplateDoesNotExist home.html`, ensure `templates/home.html` exists and `TEMPLATES['DIRS']` points to the correct folder (done in `config/settings.py`).
- If an import error complains about missing packages, install them into the active virtualenv (e.g. `opencv-python`, `Pillow`).

## Next steps

- Secure environment variables, update allowed hosts, and configure a proper production server (Gunicorn / Daphne + Nginx) when deploying.

---

If you want, I can also create a small `.env` example, add `python-dotenv` support, or prepare a `Procfile`/deployment notes.