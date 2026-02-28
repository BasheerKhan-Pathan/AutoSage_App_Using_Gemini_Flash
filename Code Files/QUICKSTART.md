# 🚀 Quick Start Guide - AutoSage App

Get up and running with AutoSage in just 5 minutes!

## ⚡ Fast Setup

### 1. Extract the ZIP File
Unzip the downloaded file to any location on your computer.

### 2. Open Terminal/Command Prompt
Navigate to the extracted folder:
```bash
cd path/to/AutoSage
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get Your Google API Key

**Quick Steps:**
1. Go to: https://ai.google.dev/gemini-api/docs/api-key
2. Sign in with Google
3. Click "Create API Key"
4. Copy the key

### 5. Create .env File

**Windows (Command Prompt):**
```cmd
copy .env.example .env
notepad .env
```

**macOS/Linux (Terminal):**
```bash
cp .env.example .env
nano .env
```

Paste your API key:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

Save and close the file.

### 6. Run the App
```bash
streamlit run app.py
```

That's it! Your browser will open automatically at http://localhost:8501

## 📸 Quick Test

1. Find any vehicle image online or use your own photo
2. Save it to your computer
3. In AutoSage, click "Browse files"
4. Select the vehicle image
5. Click "Analyze Vehicle"
6. See the magic happen!

## 🆘 Quick Troubleshooting

**Problem**: Command 'pip' not found
**Solution**: Use `pip3` instead: `pip3 install -r requirements.txt`

**Problem**: Command 'streamlit' not found
**Solution**: Try: `python -m streamlit run app.py`

**Problem**: API Error
**Solution**: Double-check your API key in the `.env` file

**Problem**: Port already in use
**Solution**: Run on different port: `streamlit run app.py --server.port 8502`

## 💡 Pro Tips

- Use clear, well-lit vehicle images for best results
- The app works best with front/side view photos
- Internet connection required for AI analysis
- Keep your API key private and never share it

## 📱 First Time Users

1. Start with a well-known vehicle (like Toyota Camry, Honda Civic)
2. Upload a clear image from the internet
3. Click "Analyze Vehicle" and wait 5-10 seconds
4. Read through all the information provided
5. Try different vehicles to see the variety of responses!

## 🎯 What You Can Analyze

- ✅ Motorcycles
- ✅ Scooters
- ✅ Cars
- ✅ SUVs
- ✅ Trucks
- ✅ Electric vehicles
- ✅ Vintage cars
- ✅ Luxury vehicles

## ⏱️ Expected Response Time

- Image upload: Instant
- AI Analysis: 5-15 seconds
- Results display: Instant

## 🔄 Multiple Analyses

You can analyze unlimited vehicles! Just:
1. Upload a new image
2. Click "Analyze Vehicle" again
3. Get new results

No need to refresh the page!

---

**Need more help?** Check the full README.md file for detailed documentation.

**Ready to start?** Run `streamlit run app.py` and enjoy! 🚗✨
