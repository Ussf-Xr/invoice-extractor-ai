#!/bin/bash

echo "🚀 Invoice Extractor AI - Deployment Script"
echo "============================================="

# Check if we're in the right directory
if [ ! -f "backend/main.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

echo "✅ Project structure verified"

# Check if Git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit: Invoice Extractor AI"
fi

echo ""
echo "🌐 Choose your deployment platform:"
echo "1. Railway (Recommended)"
echo "2. Render (Free tier)"
echo "3. Heroku (Paid)"
echo "4. Manual deployment instructions"
echo ""

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo ""
        echo "🚂 Railway Deployment Instructions:"
        echo "=================================="
        echo "1. Go to https://railway.app"
        echo "2. Sign in with your account"
        echo "3. Click 'New Project'"
        echo "4. Choose 'Deploy from GitHub repo'"
        echo "5. Connect your GitHub repository"
        echo "6. Set environment variables:"
        echo "   OPENAI_API_KEY=your_openai_api_key_here"
        echo ""
        echo "7. Deploy and get your URL"
        echo "8. Update your Google Apps Script with the new URL"
        ;;
    2)
        echo ""
        echo "🎨 Render Deployment Instructions:"
        echo "================================="
        echo "1. Go to https://render.com"
        echo "2. Sign up/Login with GitHub"
        echo "3. Click 'New Web Service'"
        echo "4. Connect your GitHub repository"
        echo "5. Configure:"
        echo "   - Name: invoice-extractor-ai"
        echo "   - Build Command: pip install -r requirements.txt"
        echo "   - Start Command: uvicorn main:app --host 0.0.0.0 --port \$PORT"
        echo "6. Add environment variable:"
        echo "   OPENAI_API_KEY=your_openai_api_key_here"
        echo "7. Deploy and get your URL"
        ;;
    3)
        echo ""
        echo "🦊 Heroku Deployment Instructions:"
        echo "================================="
        echo "1. Install Heroku CLI: brew install heroku"
        echo "2. Login: heroku login"
        echo "3. Create app: heroku create your-app-name"
        echo "4. Deploy:"
        echo "   cd backend"
        echo "   git push heroku main"
        echo "5. Set environment variable:"
        echo "   heroku config:set OPENAI_API_KEY=your_openai_api_key_here"
        ;;
    4)
        echo ""
        echo "📋 Manual Deployment Steps:"
        echo "==========================="
        echo "1. Push your code to GitHub:"
        echo "   git remote add origin https://github.com/yourusername/invoice-extractor-ai.git"
        echo "   git push -u origin main"
        echo ""
        echo "2. Choose a deployment platform:"
        echo "   - Railway: https://railway.app"
        echo "   - Render: https://render.com"
        echo "   - Heroku: https://heroku.com"
        echo "   - DigitalOcean: https://digitalocean.com"
        echo ""
        echo "3. Set environment variables:"
        echo "   OPENAI_API_KEY=your_openai_api_key_here"
        echo ""
        echo "4. Update Google Apps Script with your deployment URL"
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "🎉 After deployment, don't forget to:"
echo "1. Test your API endpoint: https://your-app-url.com/health"
echo "2. Update your Google Apps Script Code.gs with the new backend URL"
echo "3. Test the complete workflow in Google Sheets"
echo ""
echo "📖 For detailed instructions, see DEPLOYMENT.md" 