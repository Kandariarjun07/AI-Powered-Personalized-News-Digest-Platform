# AI-Powered Personalized News Digest Platform

## Setup

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables:**
    *   Copy `.env.example` to `.env`.
    *   Fill in `MONGO_URI`, `OPENROUTER_API_KEY`, and `EMAIL_RECIPIENT`.
    *   Ensure `RSS_FEED_URLS` are populated (default templates provided).

3.  **Google Credentials:**
    *   Place your `credentials.json` (OAuth 2.0 Client IDs) in this root directory.
    *   The first run will attempt to generate `token.json` via browser authentication if it doesn't exist.

## Usage

Run the scheduler (set to 01:15 AM):
```bash
python scheduler.py
```

Run a one-off execution immediately:
```bash
python main.py
```
