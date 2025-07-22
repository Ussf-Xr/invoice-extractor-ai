# Invoice Extractor AI - SaaS Project

A complete SaaS solution for extracting structured data from invoice text using AI. The project consists of a FastAPI backend with OpenAI GPT-4 integration and a Google Apps Script frontend for Google Sheets.

## Project Structure

```
Invoiceextractorai/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── models.py            # Pydantic models
│   ├── ai_invoice.py        # OpenAI integration
│   ├── requirements.txt     # Python dependencies
│   └── env.example          # Environment variables template
├── frontend/
│   ├── Code.gs              # Google Apps Script main file
│   └── Sidebar.html         # HTML sidebar interface
└── README.md                # This file
```

## Features

- **AI-Powered Analysis**: Uses OpenAI GPT-4 to extract invoice data
- **Structured Output**: Extracts invoice_id, vendor, total, and date
- **Google Sheets Integration**: Direct integration with Google Sheets
- **Error Handling**: Comprehensive error handling and validation
- **Modern UI**: Clean, responsive interface

## Backend Setup

### Prerequisites

- Python 3.8+
- OpenAI API key
- pip (Python package manager)

### Installation

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp env.example .env
   ```
   
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_openai_api_key_here
   ```

### Running Locally

1. **Start the development server:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Test the API:**
   - Open your browser to `http://localhost:8000`
   - View the interactive API documentation at `http://localhost:8000/docs`
   - Test the `/analyze-invoice` endpoint

### API Endpoints

- `GET /` - Health check
- `GET /health` - Detailed health status
- `POST /analyze-invoice` - Analyze invoice text

#### Example API Request

```bash
curl -X POST "http://localhost:8000/analyze-invoice" \
     -H "Content-Type: application/json" \
     -d '{
       "text": "INVOICE #INV-001\nABC Company\nTotal: $150.00\nDate: 2024-01-15"
     }'
```

#### Example API Response

```json
{
  "invoice_id": "INV-001",
  "vendor": "ABC Company",
  "total": 150.0,
  "date": "2024-01-15",
  "success": true,
  "error_message": null
}
```

### Deployment Options

#### Option 1: Railway (Recommended for MVP)

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login and deploy:**
   ```bash
   railway login
   railway init
   railway up
   ```

3. **Set environment variables in Railway dashboard:**
   - `OPENAI_API_KEY`

#### Option 2: Heroku

1. **Install Heroku CLI and create app:**
   ```bash
   heroku create your-app-name
   ```

2. **Add buildpack:**
   ```bash
   heroku buildpacks:set heroku/python
   ```

3. **Deploy:**
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

4. **Set environment variables:**
   ```bash
   heroku config:set OPENAI_API_KEY=your_api_key
   ```

#### Option 3: DigitalOcean App Platform

1. **Create app in DigitalOcean dashboard**
2. **Connect your GitHub repository**
3. **Set environment variables**
4. **Deploy**

## Frontend Setup (Google Apps Script)

### Prerequisites

- Google account
- Access to Google Sheets
- Deployed backend URL

### Installation

1. **Open Google Apps Script:**
   - Go to [script.google.com](https://script.google.com)
   - Click "New Project"

2. **Create the files:**
   - Rename the default `Code.gs` file
   - Copy the contents from `frontend/Code.gs`
   - Create a new HTML file named `Sidebar.html`
   - Copy the contents from `frontend/Sidebar.html`

3. **Update the backend URL:**
   - In `Code.gs`, replace `https://your-backend-url.com` with your actual deployed backend URL

4. **Save and authorize:**
   - Click "Save" (Ctrl+S)
   - Click "Deploy" → "New deployment"
   - Choose "Web app" as the type
   - Set "Execute as" to "Me"
   - Set "Who has access" to "Anyone"
   - Click "Deploy"

### Testing the Add-on

1. **Open Google Sheets**
2. **Go to Extensions → Apps Script**
3. **Run the `onOpen` function** (this creates the menu)
4. **Refresh your Google Sheets page**
5. **You should see "Invoice Extractor AI" in the menu**

### Using the Add-on

1. **Open a Google Sheet**
2. **Click "Invoice Extractor AI" → "Open Invoice Analyzer"**
3. **Click "Setup Sheet Headers"** (first time only)
4. **Paste invoice text in the textarea**
5. **Click "Analyze Invoice"**
6. **The extracted data will be inserted as a new row**

## Sample Invoice Text

Here's a sample invoice text you can use for testing:

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

## Error Handling

### Backend Errors

- **400 Bad Request**: Invalid input or missing text
- **500 Internal Server Error**: OpenAI API issues or server errors
- **422 Validation Error**: Invalid JSON format

### Frontend Errors

- **Network Errors**: Check backend URL and connectivity
- **API Errors**: Check OpenAI API key and quota
- **Sheet Errors**: Check Google Sheets permissions

## Security Considerations

1. **API Keys**: Never commit API keys to version control
2. **CORS**: Configure CORS properly for production
3. **Rate Limiting**: Implement rate limiting for production use
4. **Input Validation**: All inputs are validated and sanitized
5. **Error Messages**: Avoid exposing sensitive information in error messages

## Troubleshooting

### Backend Issues

1. **OpenAI API Key Error:**
   - Verify your API key is correct
   - Check if you have sufficient credits
   - Ensure the key has access to GPT-4

2. **Import Errors:**
   - Make sure all dependencies are installed
   - Check Python version compatibility

3. **Port Issues:**
   - Change the port in `main.py` if 8000 is in use
   - Use `--port 8080` with uvicorn

### Frontend Issues

1. **Menu Not Appearing:**
   - Run the `onOpen` function manually
   - Refresh the Google Sheets page
   - Check for JavaScript errors in browser console

2. **API Calls Failing:**
   - Verify the backend URL is correct
   - Check if the backend is running
   - Ensure CORS is properly configured

3. **Data Not Inserting:**
   - Check Google Sheets permissions
   - Verify the sheet is not protected
   - Run `setupSheetHeaders` first

## Development

### Adding New Fields

To extract additional invoice fields:

1. **Update `models.py`:**
   - Add new fields to `InvoiceAnalysisRequest` and `InvoiceAnalysisResponse`

2. **Update `ai_invoice.py`:**
   - Modify the system prompt to include new fields
   - Update the parsing logic

3. **Update `Code.gs`:**
   - Add new fields to the data insertion logic

4. **Update `Sidebar.html`:**
   - Add new fields to the results display

### Testing

1. **Backend Testing:**
   ```bash
   # Install pytest
   pip install pytest
   
   # Run tests (create test files first)
   pytest
   ```

2. **Frontend Testing:**
   - Use the Apps Script debugger
   - Check browser console for errors
   - Test with various invoice formats

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the error logs
3. Test with the sample invoice text
4. Verify all configuration steps

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request 