# ROHIT AUTO FORWARDER — starter

This is a starter scaffold, not a finished hosted service.

## Files
- `index.html`, `style.css`, `script.js`: browser dashboard mock-up.
- `app.py`: small Flask health/status backend.
- `forwarder.py`: Telethon forwarding engine scaffold (not connected to a live account).
- `requirements.txt`: Python dependencies.

## Important
GitHub Pages hosts only the static dashboard; it does not run Python.
A Python backend needs a separate server. Free hosting may sleep or stop.
Never paste your Telegram OTP, 2-step password, API hash, bot token, or session file into GitHub.
Use only channels and groups where you have permission to copy/send messages.

## Local test
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
