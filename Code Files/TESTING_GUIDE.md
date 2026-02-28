# AutoSage - Testing Guide

## 🧪 How to Test AutoSage

This guide helps you verify that AutoSage is working correctly after installation.

## ✅ Pre-Testing Checklist

Before testing, ensure:
- [ ] Python 3.8+ is installed
- [ ] All dependencies are installed (`pip install -r requirements.txt`)
- [ ] .env file exists with valid Google API key
- [ ] Internet connection is active

## 🚀 Quick Functionality Test

### Test 1: Application Launch

**Steps:**
1. Open terminal/command prompt
2. Navigate to project folder
3. Run: `streamlit run app.py`

**Expected Result:**
- Terminal shows "You can now view your Streamlit app in your browser"
- Browser opens automatically to http://localhost:8501
- Page title shows "AutoSage - Vehicle Expert"

**If Failed:**
- Check Python installation
- Verify streamlit is installed
- Try: `python -m streamlit run app.py`

---

### Test 2: UI Components

**Steps:**
1. Launch the application
2. Observe the interface

**Expected Result:**
- Title "🚗 AutoSage App" is visible
- Upload section on the left
- Info section on the right
- "Analyze Vehicle" button present
- Clean, professional design

**If Failed:**
- Check console for errors
- Clear browser cache
- Try different browser

---

### Test 3: Image Upload

**Steps:**
1. Click "Browse files" button
2. Select a vehicle image (JPG or PNG)
3. Observe the upload

**Expected Result:**
- File picker dialog opens
- Image displays after selection
- Caption "Uploaded Vehicle Image" appears
- No errors in console

**If Failed:**
- Verify image format (JPG, JPEG, or PNG only)
- Check file size (keep under 10MB)
- Try different image

---

### Test 4: API Integration

**Steps:**
1. Upload a clear vehicle image (e.g., car or motorcycle)
2. Click "Analyze Vehicle" button
3. Wait for response

**Expected Result:**
- Spinner shows "AI is analyzing..."
- Response appears in 5-15 seconds
- Results include:
  - Brand & Model
  - Key Features
  - Mileage
  - Price Range
  - Pros & Cons
- Success message appears

**If Failed:**
- Check .env file for correct API key
- Verify internet connection
- Check Google AI Studio for API quota
- Review error message in app

---

## 🎯 Detailed Test Cases

### Test Case 1: Popular Car Recognition

**Vehicle:** Toyota Camry
**Test Image:** Clear front/side view
**Expected Output:**
- Correct brand identification (Toyota)
- Correct model (Camry)
- Year range if visible
- Accurate specifications
- Competitive price range

---

### Test Case 2: Motorcycle Analysis

**Vehicle:** Any popular motorcycle (e.g., Yamaha R15, Honda CBR)
**Test Image:** Clear profile shot
**Expected Output:**
- Identifies as two-wheeler
- Brand and model name
- Engine capacity
- Mileage information
- Target audience (sports, commuter, etc.)

---

### Test Case 3: Electric Vehicle

**Vehicle:** Tesla Model 3, Nissan Leaf, etc.
**Test Image:** Clear exterior shot
**Expected Output:**
- Identifies as electric vehicle
- Battery range information
- Eco-friendly benefits mentioned
- Charging information
- Environmental impact notes

---

### Test Case 4: Vintage/Classic Vehicle

**Vehicle:** Classic car (e.g., 1960s Mustang)
**Test Image:** Well-preserved classic
**Expected Output:**
- Historical context
- Year/era identification
- Collector value information
- Classic features noted
- Restoration considerations

---

## 🚫 Error Handling Tests

### Error Test 1: No Image Upload

**Steps:**
1. Launch app
2. Click "Analyze Vehicle" without uploading image

**Expected Result:**
- Warning message: "Please upload a vehicle image first"
- No API call made
- App remains stable

---

### Error Test 2: Invalid API Key

**Steps:**
1. Edit .env file with incorrect API key
2. Upload image and analyze

**Expected Result:**
- Error message about API authentication
- Clear indication of API key issue
- Helpful message to check .env file

---

### Error Test 3: Network Disconnection

**Steps:**
1. Disconnect internet
2. Try to analyze vehicle

**Expected Result:**
- Network error message
- App doesn't crash
- User can retry after reconnection

---

### Error Test 4: Unsupported File Format

**Steps:**
1. Try to upload .gif, .bmp, or other format

**Expected Result:**
- File picker only shows supported formats
- Or clear error if unsupported file selected

---

## 📊 Performance Tests

### Performance Test 1: Response Time

**Method:**
1. Upload standard car image
2. Time from click to response

**Acceptable Range:**
- Minimum: 3 seconds
- Maximum: 20 seconds
- Average: 8-12 seconds

---

### Performance Test 2: Large Image Handling

**Method:**
1. Upload high-resolution image (3-5MB)
2. Observe processing

**Expected:**
- App handles without crashing
- Processing time may increase slightly
- Results still accurate

---

### Performance Test 3: Multiple Analyses

**Method:**
1. Analyze 5 different vehicles in succession
2. Observe consistency

**Expected:**
- Each analysis completes successfully
- No degradation in performance
- No memory issues

---

## 🔍 Quality Assurance

### Quality Test 1: Accuracy Check

**Method:**
1. Upload image of known vehicle
2. Compare AI response with actual specs

**Evaluation:**
- Brand/Model: Should be 95%+ accurate
- Specifications: Should be generally accurate
- Price: Should be in reasonable range
- Features: Should match major features

---

### Quality Test 2: Consistency Check

**Method:**
1. Upload same vehicle image twice
2. Compare responses

**Expected:**
- Core information remains consistent
- Minor variations acceptable in wording
- Key facts should match

---

## 📝 Test Results Template

Use this template to record your testing:

```
TEST DATE: _______________
TESTER: _______________

FUNCTIONALITY TESTS:
[ ] Application Launch - PASS/FAIL
[ ] UI Components - PASS/FAIL
[ ] Image Upload - PASS/FAIL
[ ] API Integration - PASS/FAIL

DETAILED TESTS:
[ ] Popular Car Recognition - PASS/FAIL
[ ] Motorcycle Analysis - PASS/FAIL
[ ] Electric Vehicle - PASS/FAIL
[ ] Vintage Vehicle - PASS/FAIL

ERROR HANDLING:
[ ] No Image Upload - PASS/FAIL
[ ] Invalid API Key - PASS/FAIL
[ ] Network Disconnection - PASS/FAIL
[ ] Unsupported Format - PASS/FAIL

PERFORMANCE:
Average Response Time: _______ seconds
Large Image Handling: PASS/FAIL
Multiple Analyses: PASS/FAIL

QUALITY:
Accuracy: _______%
Consistency: PASS/FAIL

OVERALL: PASS/FAIL

NOTES:
_________________________________
_________________________________
_________________________________
```

## 🐛 Common Issues & Solutions

### Issue: Slow Response Time

**Possible Causes:**
- Slow internet connection
- Google API server load
- Large image file

**Solutions:**
- Check internet speed
- Try during off-peak hours
- Resize images before upload

---

### Issue: Inaccurate Results

**Possible Causes:**
- Poor image quality
- Unusual angle
- Modified/custom vehicle
- Obscure model

**Solutions:**
- Use clearer images
- Try front/side view
- Use stock photos for testing
- Test with popular models first

---

### Issue: App Crashes

**Possible Causes:**
- Memory issues
- Corrupted installation
- Incompatible Python version

**Solutions:**
- Restart the application
- Reinstall dependencies
- Check Python version (3.8+)
- Clear browser cache

---

## ✨ Best Practices for Testing

1. **Start Simple**: Test with well-known vehicles first
2. **Use Quality Images**: Clear, well-lit photos work best
3. **Test Variety**: Try different vehicle types
4. **Document Results**: Keep notes of issues found
5. **Test Regularly**: Verify after any code changes
6. **Check Logs**: Review terminal output for errors

## 📞 Reporting Issues

If you find bugs during testing:

1. **Document the Issue:**
   - What you were doing
   - What you expected
   - What actually happened
   - Error messages (if any)

2. **Gather Information:**
   - Python version
   - OS (Windows/Mac/Linux)
   - Browser used
   - Screenshot of error

3. **Check Troubleshooting:**
   - Review README.md
   - Check SETUP_INSTRUCTIONS.txt
   - Verify .env configuration

## 🎯 Acceptance Criteria

AutoSage is working correctly when:

- ✅ Application launches without errors
- ✅ UI displays properly
- ✅ Images upload successfully
- ✅ API returns detailed vehicle information
- ✅ Error messages are clear and helpful
- ✅ Performance is within acceptable range
- ✅ Results are generally accurate
- ✅ App remains stable during use

---

**Happy Testing! 🧪**

*Remember: Perfect is the enemy of good. The AI won't be 100% accurate on every vehicle, but it should provide useful information most of the time.*
