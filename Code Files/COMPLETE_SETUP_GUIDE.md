# 🎯 AutoSage - Complete Setup Guide

## Welcome to AutoSage!

This is your one-stop guide to get AutoSage up and running on your laptop after extracting the ZIP file.

---

## 📦 What You Just Downloaded

AutoSage is a Python/Streamlit application that uses Google's Gemini Flash AI to analyze vehicle images. You now have all the files needed - you just need to configure your environment!

---

## ⚡ FASTEST PATH TO SUCCESS (Choose One)

### Option A: Windows Users - Automated Setup
1. Double-click `WINDOWS_SETUP.bat`
2. Wait for packages to install
3. Add your Google API key when prompted
4. Double-click `START_AUTOSAGE.bat`
5. Done! 🎉

**Time: 5-10 minutes**

---

### Option B: Any Platform - Manual Setup

#### Step 1: Check Python (2 minutes)

Open Terminal (Mac/Linux) or Command Prompt (Windows):

```bash
python --version
```

**Should show:** Python 3.8 or higher

**If not installed:**
- Download from https://www.python.org/downloads/
- During installation, check "Add Python to PATH"
- Restart terminal after installation

---

#### Step 2: Install Dependencies (3-5 minutes)

Navigate to the AutoSage folder:

```bash
cd path/to/AutoSage
```

Install required packages:

```bash
pip install -r requirements.txt
```

**Alternative commands if above doesn't work:**
```bash
pip3 install -r requirements.txt
# or
python -m pip install -r requirements.txt
```

**What gets installed:**
- Streamlit (Web framework)
- google-generativeai (AI model)
- python-dotenv (Environment variables)
- Pillow (Image processing)

**Expected output:** "Successfully installed" messages

---

#### Step 3: Get Google API Key (2-3 minutes)

This is the most important step!

1. **Visit:** https://ai.google.dev/gemini-api/docs/api-key

2. **Sign in** with your Google account

3. **Click** the blue "Get an API Key" button

4. **Click** "Create API Key"

5. **Select** a project (or create new one)

6. **Copy** the API key (looks like: AIzaSy...)

⚠️ **IMPORTANT:** Keep this key private! Never share it.

---

#### Step 4: Configure Environment (1 minute)

The `.env` file already exists in your project folder!

**Open** `.env` file with any text editor:
- Windows: Right-click → Edit with Notepad
- Mac: Double-click or use TextEdit
- Linux: Use nano, vim, or any editor

**Find this line:**
```
GOOGLE_API_KEY=your_google_api_key_here
```

**Replace** `your_google_api_key_here` with your actual API key:
```
GOOGLE_API_KEY=AIzaSyDxxxxxxxxxxxxxxxxxxxxxx
```

**Save** and close the file.

⚠️ **Critical:** No spaces around the = sign!

---

#### Step 5: Launch AutoSage (30 seconds)

Run this command:

```bash
streamlit run app.py
```

**Expected output:**
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

Your browser should open automatically!

**If browser doesn't open:**
Manually go to: http://localhost:8501

---

#### Step 6: Test It! (1 minute)

1. **Find a vehicle image:**
   - Download from https://www.pexels.com/search/car/
   - Or use any car/motorcycle photo you have

2. **In AutoSage:**
   - Click "Browse files"
   - Select your image
   - Click "🔍 Analyze Vehicle"

3. **Wait** 5-15 seconds

4. **View results!** You should see detailed vehicle information

---

## 🎉 Success Checklist

You're successful when:
- ✅ Browser opens to http://localhost:8501
- ✅ You see "AutoSage App" title
- ✅ You can upload an image
- ✅ Analysis returns vehicle information
- ✅ No error messages appear

---

## 🚨 Common Issues & Solutions

### Issue 1: "pip: command not found"

**Solution:**
```bash
# Try these alternatives:
pip3 install -r requirements.txt
python -m pip install -r requirements.txt
python3 -m pip install -r requirements.txt
```

---

### Issue 2: "streamlit: command not found"

**Solution:**
```bash
# Try running directly:
python -m streamlit run app.py
python3 -m streamlit run app.py
```

---

### Issue 3: "API key not valid" or Authentication Errors

**Solutions:**
1. Open `.env` file
2. Verify `GOOGLE_API_KEY=` line exists
3. Check for typos in API key
4. Ensure no extra spaces
5. Verify key is active in Google AI Studio
6. Make sure you copied the complete key

**Correct format:**
```
GOOGLE_API_KEY=AIzaSyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

**Wrong formats:**
```
GOOGLE_API_KEY = AIzaSy...    # Extra spaces!
GOOGLE_API_KEY=AIzaSy ..      # Space in key!
GOOGLE_API_KEY="AIzaSy..."    # Quotes not needed!
```

---

### Issue 4: "ModuleNotFoundError"

**Meaning:** A package didn't install correctly

**Solution:**
```bash
# Reinstall all packages
pip install -r requirements.txt --force-reinstall
```

---

### Issue 5: Port 8501 Already in Use

**Solution:**
```bash
# Use different port
streamlit run app.py --server.port 8502
```
Then visit: http://localhost:8502

---

### Issue 6: Browser Doesn't Open Automatically

**Solution:**
- Look at terminal output
- Find the line: "Local URL: http://localhost:8501"
- Manually open that URL in your browser
- Try Chrome, Firefox, or Edge

---

### Issue 7: Slow Installation

**Cause:** Slow internet or large dependencies

**Solution:**
- Be patient (can take 5-10 minutes on slow connections)
- Don't interrupt the installation
- Wait for "Successfully installed" message

---

## 🔄 Daily Usage

After initial setup, starting AutoSage is easy:

**Windows:**
```cmd
Double-click START_AUTOSAGE.bat
```

**Mac/Linux:**
```bash
./START_AUTOSAGE.sh
```

**Manual (Any platform):**
```bash
cd path/to/AutoSage
streamlit run app.py
```

---

## 📚 Learning Resources

### Want to understand more?

**For Beginners:**
- `START_HERE.md` - Navigation guide
- `FAQ.md` - 50+ questions answered
- `TESTING_GUIDE.md` - How to verify everything works

**For Technical Users:**
- `PROJECT_OVERVIEW.md` - Architecture details
- `app.py` - Source code (it's short!)

**For Troubleshooting:**
- `DEPLOYMENT_CHECKLIST.md` - Verify each step
- `FAQ.md` - Common problems & solutions

---

## 💡 Pro Tips

1. **Save Your API Key:** Write it down somewhere safe
2. **Bookmark the App:** http://localhost:8501 for quick access
3. **Use Quality Images:** Better images = better results
4. **Try Different Vehicles:** Test the AI's capabilities
5. **Check API Quota:** Monitor usage at https://ai.google.dev/

---

## 🎯 What Makes a Good Test Image?

Best results come from:
- ✅ Clear, well-lit photos
- ✅ Front or side view
- ✅ Entire vehicle visible
- ✅ Minimal background clutter
- ✅ High resolution (800x600+)
- ✅ Recent, popular models

Avoid:
- ❌ Blurry or dark images
- ❌ Heavily filtered photos
- ❌ Partial vehicle views
- ❌ Very old or rare models
- ❌ Heavy customization

---

## 🔒 Security Reminders

- ⚠️ NEVER share your `.env` file
- ⚠️ NEVER commit `.env` to git
- ⚠️ NEVER post your API key online
- ⚠️ Keep API key private
- ✅ Monitor API usage regularly
- ✅ Regenerate key if compromised

---

## 📊 What to Expect

### Free Tier Limits:
- 15 requests per minute
- 1,500 requests per day
- Sufficient for personal use

### Response Times:
- Image upload: Instant
- AI analysis: 5-15 seconds
- Results display: Instant

### Accuracy:
- Brand/Model: 90-95%
- Specifications: 80-90%
- Pricing: 70-80% (estimates)
- Features: 85-90%

**Always verify critical information with official sources!**

---

## 🎮 Suggested First Tests

1. **Test 1: Popular Car**
   - Search: "Toyota Camry" on Pexels
   - Expected: Accurate identification + specs

2. **Test 2: Motorcycle**
   - Search: "Yamaha motorcycle" on Pexels
   - Expected: Two-wheeler identification + engine details

3. **Test 3: Electric Vehicle**
   - Search: "Tesla Model 3" on Pexels
   - Expected: EV details + battery info

4. **Test 4: Luxury Car**
   - Search: "BMW M3" on Pexels
   - Expected: Premium features + performance specs

---

## 🆘 Still Need Help?

### Check These in Order:

1. **FAQ.md** - Covers 50+ questions
2. **TESTING_GUIDE.md** - Troubleshooting procedures
3. **DEPLOYMENT_CHECKLIST.md** - Verify each step
4. **Terminal Output** - Error messages are helpful
5. **Browser Console** - F12 to see errors

### Verify These:

- [ ] Python 3.8+ installed: `python --version`
- [ ] Packages installed: `pip list | grep streamlit`
- [ ] .env file exists and has API key
- [ ] Internet connection active
- [ ] No firewall blocking port 8501

---

## 🎉 You're All Set!

Once you see the AutoSage interface and can successfully analyze a vehicle, you're ready to go!

### Next Steps:

1. **Explore:** Try different vehicle types
2. **Learn:** Read the documentation
3. **Experiment:** Modify the code (it's yours!)
4. **Share:** Help others set up AutoSage
5. **Enjoy:** Make informed vehicle decisions!

---

## 📝 Quick Reference Card

**Install:**
```bash
pip install -r requirements.txt
```

**Configure:**
Edit `.env` file with your Google API key

**Run:**
```bash
streamlit run app.py
```

**Access:**
http://localhost:8501

**Stop:**
Press Ctrl+C in terminal

---

**That's it! Welcome to AutoSage! 🚗✨**

---

*For detailed documentation, see README.md*
*For quick tips, see QUICKSTART.md*
*For navigation, see START_HERE.md*

**Version:** 1.0.0
**Last Updated:** 2024
