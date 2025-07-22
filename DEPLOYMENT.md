# 🚀 Deployment Guide

## Quick Deployment Options

### Option 1: Railway (Recommended - 5 minutes)

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway:**
   ```bash
   railway login
   ```

3. **Deploy from backend directory:**
   ```bash
   cd backend
   railway init
   railway up
   ```

4. **Set environment variables in Railway dashboard:**
   - Go to your project in Railway
   - Click "Variables" tab
   - Add: `OPENAI_API_KEY=your_openai_api_key_here`

5. **Get your deployment URL:**
   - Railway will give you a URL like: `https://your-app-name.railway.app`

### Option 2: Render (Free tier available)

1. **Go to [render.com](https://render.com)**
2. **Create new Web Service**
3. **Connect your GitHub repository**
4. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables:** Add your OpenAI API key

### Option 3: Heroku (Free tier discontinued)

1. **Install Heroku CLI:**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   ```

2. **Login and create app:**
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Deploy:**
   ```bash
   cd backend
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

4. **Set environment variables:**
   ```bash
   heroku config:set OPENAI_API_KEY=your_openai_api_key_here
   ```

## After Deployment

### 1. Test Your Deployed API

Once deployed, test your API:

```bash
# Test health endpoint
curl https://your-app-url.com/health

# Test invoice analysis
curl -X POST "https://your-app-url.com/analyze-invoice" \
     -H "Content-Type: application/json" \
     -d '{
       "text": "INVOICE #INV-001\nABC Company\nTotal: $150.00\nDate: 2024-01-15"
     }'
```

### 2. Update Google Apps Script

In your Google Apps Script `Code.gs`, update the backend URL:

```javascript
// Replace with your actual deployed URL
const BACKEND_URL = 'https://your-app-url.com';
```

### 3. Test the Complete Flow

1. Open Google Sheets
2. Go to Extensions → Apps Script
3. Run the `onOpen` function
4. Refresh Google Sheets
5. Click "Invoice Extractor AI" → "Open Invoice Analyzer"
6. Test with sample invoice text

## Sample Invoice Text for Testing

```
INVOICE

Invoice Number: INV-2024-001
Date: January 15, 2024

From:
ABC Company Inc.
123 Business Street
City, State 12345

To:
XYZ Corporation
456 Corporate Avenue
Business City, BC 67890

Description:
- Web Development Services: $1,200.00
- Hosting (Monthly): $50.00
- Domain Registration: $15.00

Subtotal: $1,265.00
Tax (8.5%): $107.53
Total: $1,372.53

Payment Terms: Net 30
Due Date: February 14, 2024
```

## Troubleshooting

### Common Issues:

1. **CORS Errors:**
   - The backend already includes CORS middleware
   - If issues persist, check your deployment platform's CORS settings

2. **API Key Issues:**
   - Verify the API key is set correctly in your deployment platform
   - Check if you have sufficient OpenAI credits

3. **Port Issues:**
   - Most platforms use `$PORT` environment variable
   - The code is already configured for this

4. **Import Errors:**
   - All dependencies are in `requirements.txt`
   - The deployment platforms will install them automatically

## Performance Optimization (Optional)

For production use, consider:

1. **Add Rate Limiting:**
   ```python
   # Add to requirements.txt
   slowapi==0.1.9
   ```

2. **Add Caching:**
   ```python
   # Add to requirements.txt
   redis==5.0.1
   ```

3. **Add Monitoring:**
   ```python
   # Add to requirements.txt
   sentry-sdk[fastapi]==1.40.0
   ```

## Security Checklist

- ✅ API key is in environment variables
- ✅ CORS is properly configured
- ✅ Input validation is implemented
- ✅ Error handling is comprehensive
- ✅ HTTPS is enforced (on deployment platforms)

## Next Steps

1. **Deploy using one of the options above**
2. **Update your Google Apps Script with the new URL**
3. **Test the complete workflow**
4. **Share with users!**

Your SaaS is ready to go! 🎉 