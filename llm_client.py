import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def generate_newsletter(articles):
    """
    Sends the gathered news to Google's Gemini AI to write a professional newsletter.
    """
    
    if not articles:
        print("⚠️ No articles provided to the AI. Skipping generation.")
        return None

    # Format the articles into a simple text list for the AI to read
    articles_data = ""
    for i, art in enumerate(articles):
        articles_data += f"""
        --- Story {i+1} ---
        Headline: {art.get('title')}
        Source: {art.get('source')}
        Link: {art.get('url')}
        Image: {art.get('image_url')}
        Summary: {art.get('summary')}
        """

    # The Prompt: Instructing the AI on how to act and what to create
    system_instruction = "You are a professional technology newspaper editor."
    
    user_prompt = f"""
    Write a 'MorningByte' HTML email newsletter based on the stories below.

    ### Design Requirements:
    - Use a clean, table-based HTML layout (compatible with Gmail/Outlook).
    - Styling: Inline CSS, Sans-serif fonts, professional "Newspaper" look.
    - Header: A bold masthead titled 'MorningByte'.
    - Layout: Use horizontal separators between sections.

    ### Content Rules:
    Select exactly **20 articles** from the provided data, categorized strictly as follows:
    1. **Anime & Manga** (5 articles)
    2. **Artificial Intelligence (AI)** (5 articles)
    3. **Gaming** (5 articles)
    4. **Coding & Development** (5 articles)

    If there are not enough articles in a category to meet the quota, select the most relevant remaining tech news to fill the gap, but prioritize the specific categories requested.

    For each story:
       - Display the **Title** as a bold link.
       - If a valid 'Image' URL exists (not 'NONE'), show it (Max width: 600px, rounded corners).
       - Write a 2-sentence summary in a neutral, journalistic tone.
       - Mention the source (e.g., "via TechCrunch").

    ### Data:
    {articles_data}

    **IMPORTANT:** Output ONLY raw HTML code. Do not include markdown formatting like ```html.
    """

    print("🧠 Sending data to Google Gemini AI...")

    google_key = os.getenv("GOOGLE_API_KEY")
    if not google_key:
        print("❌ Error: GOOGLE_API_KEY is missing.")
        return None

    try:
        # Initialize Google's Generative AI Client
        client = genai.Client(api_key=google_key)
        
        # We use Gemini 3.0 Flash for its speed and context handling
        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents=[
                {"role": "user", "parts": [{"text": system_instruction}]},
                {"role": "user", "parts": [{"text": user_prompt}]}
            ]
        )
        
        # Clean up the output to ensure it's pure HTML
        html_output = response.text.replace("```html", "").replace("```", "").strip()
        
        print("✨ Newsletter HTML generated successfully!")
        return html_output

    except Exception as e:
        print(f"❌ AI Generation Failed: {e}")
        return "<h1>Details Unavailable</h1><p>Sorry, the AI could not generate the newsletter today.</p>"
