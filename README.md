# 🚗 AutoSage - AI-Powered Vehicle Information Assistant

AutoSage is a cutting-edge application powered by Google's Gemini Flash technology, designed to provide comprehensive information on two-wheeler and four-wheeler vehicles. This vehicle expert tool offers detailed specifications, reviews, and comparisons, helping users make informed decisions about their next vehicle purchase.

## ✨ Features

- 🔍 **Vehicle Recognition**: Upload any vehicle image and get instant identification
- 📊 **Detailed Specifications**: Get comprehensive information about engine, features, and performance
- 💰 **Price Information**: Receive accurate price ranges and market insights
- ⚖️ **Pros & Cons Analysis**: Understand the advantages and disadvantages of each vehicle
- 🏆 **Competitor Comparison**: See how the vehicle compares with similar models
- 🌱 **Eco-Friendly Options**: Get insights into electric and hybrid vehicles
- 📱 **User-Friendly Interface**: Clean, intuitive design powered by Streamlit

## 🎯 Use Cases

### Scenario 1: Buying a New Motorcycle
Sarah wants to buy a new motorcycle. She uses AutoSage App with Gemini Flash to compare specs, features, and prices of various models. The app provides real-time analysis and detailed information on the latest motorcycles, helping her make an informed decision and choose the best option within her budget.

### Scenario 2: Vehicle Information & Maintenance
Users can get detailed information about vehicle specifications, which helps in understanding maintenance requirements. AutoSage provides insights into engine capacity, type, and features that are crucial for proper vehicle care.

### Scenario 3: Finding Eco-Friendly Vehicles
Emma is looking for eco-friendly vehicle options. She utilizes AutoSage App with Gemini Flash to explore electric and hybrid vehicles. The app provides insights into vehicle efficiency, environmental impact, and specifications, helping her choose a sustainable option that aligns with her green goals.

## 🛠️ Technology Stack

- **Frontend Framework**: Streamlit
- **AI Model**: Google Gemini Flash (gemini-1.5-flash)
- **Image Processing**: Pillow (PIL)
- **Environment Management**: python-dotenv
- **Language**: Python 3.8+

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.8 or higher installed
- A Google API Key for Gemini API
- pip (Python package manager)

## 🔑 Getting Google API Key

1. Visit [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key)
2. Sign in with your Google account
3. Click on **"Get an API Key"**
4. Click **"Create API Key"**
5. Select your project or create a new one
6. Copy the generated API key (you'll need this in the setup)

## 📦 Installation Instructions

### Step 1: Extract the Project

After downloading the ZIP file, extract it to your desired location on your laptop.

```bash
# Navigate to the extracted folder
cd AutoSage
```

### Step 2: Create a Virtual Environment (Recommended)

Creating a virtual environment helps isolate project dependencies.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- streamlit (Web framework)
- google-generativeai (Gemini API client)
- python-dotenv (Environment variable management)
- Pillow (Image processing)

### Step 4: Configure Environment Variables

1. Locate the `.env.example` file in the project folder
2. Create a copy and rename it to `.env`
3. Open the `.env` file in a text editor
4. Replace `your_google_api_key_here` with your actual Google API key

**Your `.env` file should look like:**
```
GOOGLE_API_KEY=AIzaSyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

⚠️ **Important**: Never share your `.env` file or commit it to version control!

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

If it doesn't open automatically, manually navigate to the URL shown in the terminal.

## 🎮 How to Use AutoSage

1. **Launch the Application**: Run `streamlit run app.py`
2. **Upload Vehicle Image**:
   - Click on "Browse files" or drag and drop an image
   - Supported formats: JPG, JPEG, PNG
   - Use clear, high-quality images for best results
3. **Analyze**: Click the "🔍 Analyze Vehicle" button
4. **View Results**: Get comprehensive information including:
   - Brand & Model identification
   - Key features and specifications
   - Mileage information
   - Price range
   - Pros and cons
   - Competitor comparison

## 📁 Project Structure

```
AutoSage/
│
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variable template
├── .env                  # Your API keys (create this file)
├── .gitignore           # Git ignore rules
├── README.md            # This file
│
└── Images/              # (Optional) Sample vehicle images for testing
```

## 🔧 Troubleshooting

### Issue: "No module named 'streamlit'"
**Solution**: Make sure you've activated your virtual environment and installed dependencies:
```bash
pip install -r requirements.txt
```

### Issue: "API key not found" or Authentication Error
**Solution**:
- Verify your `.env` file exists in the project root
- Check that `GOOGLE_API_KEY` is spelled correctly
- Ensure your API key is valid and active in Google AI Studio

### Issue: Application won't start
**Solution**:
- Check if port 8501 is already in use
- Try running on a different port: `streamlit run app.py --server.port 8502`

### Issue: "FileNotFoundError: No file uploaded"
**Solution**: Make sure to upload an image before clicking the "Analyze Vehicle" button

### Issue: Poor analysis results
**Solution**:
- Use clear, high-resolution images
- Ensure the vehicle is clearly visible in the image
- Try different angles if the first attempt doesn't work well

## 🌟 Features in Detail

### Vehicle Analysis Components

1. **Brand & Model Recognition**: AI identifies the manufacturer and specific model
2. **Specifications**: Detailed technical information about the vehicle
3. **Pricing**: Market price ranges to help with budgeting
4. **Performance Metrics**: Mileage, engine capacity, and power output
5. **Comparison**: How it stacks up against competitors
6. **Recommendations**: Who the vehicle is best suited for

## 🔒 Security Best Practices

- ✅ Never commit your `.env` file to version control
- ✅ Keep your Google API key confidential
- ✅ Use environment variables for all sensitive data
- ✅ Regularly rotate your API keys
- ✅ Monitor your API usage in Google Cloud Console

## 📊 API Usage Limits

Google Gemini Flash API has usage limits:
- Free tier: 15 requests per minute
- Monitor your usage in [Google AI Studio](https://ai.google.dev/)
- Consider upgrading if you need higher limits

## 🚀 Future Enhancements

Potential features for future versions:
- [ ] Vehicle comparison tool (compare 2-3 vehicles side by side)
- [ ] Price prediction based on age and condition
- [ ] Maintenance schedule recommendations
- [ ] Database integration to save search history
- [ ] Export results as PDF reports
- [ ] Multi-language support
- [ ] Voice input for hands-free operation

## 🤝 Support

If you encounter any issues:
1. Check the Troubleshooting section above
2. Verify your API key is correctly configured
3. Ensure all dependencies are installed
4. Check the terminal for error messages

## 📝 Requirements

### System Requirements
- **OS**: Windows 10/11, macOS 10.14+, or Linux
- **RAM**: Minimum 4GB (8GB recommended)
- **Python**: 3.8 or higher
- **Internet**: Stable connection required for API calls

### Python Packages
See `requirements.txt` for complete list

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Python-dotenv Guide](https://pypi.org/project/python-dotenv/)
- [PIL/Pillow Documentation](https://pillow.readthedocs.io/)

## 📜 License

This project is for educational purposes. Please ensure compliance with Google's Gemini API terms of service.

## 🙏 Acknowledgments

- Google Gemini AI for the powerful language model
- Streamlit for the excellent web framework
- The open-source community for various libraries used

## 📞 Contact & Feedback

For questions, suggestions, or feedback about AutoSage, please feel free to reach out or contribute to the project.

---

**Happy Vehicle Hunting! 🚗🏍️**

*AutoSage - Making vehicle decisions easier, one image at a time.*
