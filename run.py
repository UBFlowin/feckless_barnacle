import os
os.system("gunicorn app:app -b localhost:8000")

