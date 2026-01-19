# Daily Tech & Geek Culture Digest 

This is a personal automation project that curates a daily newsletter of tech, AI, gaming, and anime news. It runs completely in the cloud using **GitHub Actions**, fetches news from RSS feeds, summarizes them using **Google Gemini AI**, and sends a beautiful HTML email straight to my inbox every morning.

## How It Works

1.  **Fetch:** Every morning at 7:50 AM IST, the script wakes up and scans RSS feeds (TechCrunch, AnimeNewsNetwork, etc.) for the latest 200 articles.
2.  **Filter & Sort:** It saves them to a MongoDB database to keep track of history.
3.  **AI Magic:** It sends the article list to Google's Gemini Flash model. The AI picks the top 5 stories for **Artificial Intelligence**, **Gaming**, **Anime**, and **Coding**, then writes a crisp 2-sentence summary for each.
4.  **Deliver:** The script logs into Gmail (via OAuth) and sends a formatted 'Newspaper-style' email.

## Project Structure

- main.py: The boss. Orchestrates the whole flow step-by-step.
- 
ss_fetcher.py: The gatherer. Goes out to the internet and collects raw news.
- llm_client.py: The writer. Talks to Google Gemini to generate the content.
- email_sender.py: The postman. Handles the tricky Gmail OAuth stuff to send the email.
- db.py: The memory. Saves data to MongoDB.
- .github/workflows/daily_digest.yml: The alarm clock. Tells GitHub when to run the code.

---

## Local Setup (If you want to run it on your laptop)

You generally don't need to run this locally since it runs on GitHub, but if you want to test changes:

1.  **Install Requirements:**
    `ash
    pip install -r requirements.txt
    `

2.  **Set up Environment Variables (.env):**
    Create a .env file and add your keys:
    `ini
    MONGO_URI=mongodb+srv://...
    GOOGLE_API_KEY=AIzaSy...
    EMAIL_RECIPIENT=your_email@gmail.com
    RSS_FEED_URLS=http://feed1.com, http://feed2.com
    `

3.  **Authentication:**
    You need a credentials.json from Google Cloud Console. Run the script once, and it will open a browser to login. It saves a 	oken.json file which keeps you logged in.

4.  **Run:**
    `ash
    python main.py
    `

---

## Deployment (GitHub Actions)

This repo is configured to run automatically. You just need to set the secrets in **Settings > Secrets and variables > Actions**:

- MONGO_URI: Your database connection.
- GOOGLE_API_KEY: Your Gemini API Key.
- EMAIL_RECIPIENT: Where to send the email.
- RSS_FEED_URLS: Comma-separated list of RSS feeds.
- GMAIL_TOKEN_JSON: **Crucial.** Paste the full content of your local 	oken.json here. This is how the cloud logs in as you.

## Tech Stack
- **Language:** Python 3.12
- **AI Model:** Google Gemini 2.0 Flash
- **Database:** MongoDB Atlas
- **Automation:** GitHub Actions (Cron Job)
