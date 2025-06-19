BASIC DESCRIPTION :
Cyber Buddy 🛡️ | A real-time phishing URL and malware file scanner built using Flask and VirusTotal API. Analyze links &amp; files securely with a modern interface.

DETAILED README:
# 🛡️ Cyber Buddy – Your Online Threat Scanner

**Cyber Buddy** is your go-to web app for checking suspicious websites and files. Whether you're worried about a sketchy link or a random file someone sent you, Cyber Buddy helps you stay safe with real-time threat detection—powered by the VirusTotal API.

We’ve designed it to be simple, fast, and secure. Just paste a URL or upload a file, and we’ll scan it for phishing or malware threats and give you a clear report. No tech jargon—just the info you need.

## What It Does

-  Scan any URL for phishing, malware, or suspicious behavior  
-  Upload files (like .exe, .zip) and check them for viruses  
-  Get instant stats: how many antivirus engines flagged it as safe or dangerous  
-  Clean and modern UI with a cyberpunk vibe  
-  No personal data stored—safe and secure by design  

________________________________________________________________________

## Project Layout

CYBER_BUDDY/
│
├── frontend/         # All the HTML and CSS pages
│   ├── index.html
│   ├── scan.html
│   ├── upload.html
│   ├── result.html
│   └── styles.css
│
├── backend/          # Flask backend
│   ├── app.py
│   └── .env          # Keep your API key here (do not share)
│
├── static/           # Icons, images, spinners, etc.
├── templates/        # result.html used by Flask
├── requirements.txt
└── README.md

---

##  How to Use

### 1. Clone the Repository
IN bash :
    ** git clone https://github.com/your-username/CYBER_BUDDY.git **
    ** cd CYBER_BUDDY **

2. Get Your Free VirusTotal API Key
	•	Sign up at virustotal.com
	•	Go to your profile, copy the API key
	•	Create a .env file inside backend/ and add this:

VT_API_KEY=your_api_key_here

3. Install Python Libraries

   ** pip install -r requirements.txt **

4. Run the App

cd backend
python app.py

  Then open ** http://localhost:5000 ** in your browser 🚀

⸻

 Screenshots (Coming Soon)
	•	Landing Page
	•	URL Scan Page
	•	File Upload Page
	•	Result Page

Want to contribute? Feel free to share UI improvements or feature ideas!

⸻

🌍 Deployment Tips
	•	Frontend → Deploy on Vercel or Netlify
	•	Backend → Use Render or Railway
	•	Store .env keys as environment variables in your deployment settings

⸻

## Project Creators
  •	Aryan Sheoran – Frontend & UI Developer
	•	Vishal Yadav – Cybersecurity Researcher & Tester

This was built as part of a college cybersecurity project—but we hope it helps others too!

⸻

## License

 You’re free to use, modify, or share this project.
Just don’t forget to give us credit. 😄

⸻

Stay safe online. Think before you click.
Made with ❤️ by two curious minds

