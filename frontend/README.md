# Google Apps Script Frontend Setup

This guide will help you set up the Google Apps Script frontend for the Invoice Extractor AI project.

## Quick Setup

### 1. Create New Apps Script Project

1. Go to [script.google.com](https://script.google.com)
2. Click "New Project"
3. Rename the project to "Invoice Extractor AI"

### 2. Add the Code Files

#### Code.gs
1. Replace the default `Code.gs` content with the code from `frontend/Code.gs`
2. **Important**: Update the `BACKEND_URL` variable with your deployed backend URL:
   ```javascript
   const BACKEND_URL = 'https://your-actual-backend-url.com';
   ```

#### Sidebar.html
1. Click the "+" button next to "Files"
2. Select "HTML"
3. Name it "Sidebar"
4. Replace the content with the code from `frontend/Sidebar.html`

### 3. Save and Deploy

1. Click "Save" (Ctrl+S)
2. Click "Deploy" → "New deployment"
3. Choose "Web app" as the type
4. Set "Execute as" to "Me"
5. Set "Who has access" to "Anyone"
6. Click "Deploy"

### 4. Test the Add-on

1. Open a new Google Sheet
2. Go to Extensions → Apps Script
3. Run the `onOpen` function manually
4. Refresh the Google Sheets page
5. You should see "Invoice Extractor AI" in the menu

## Usage

### First Time Setup

1. Open a Google Sheet
2. Click "Invoice Extractor AI" → "Open Invoice Analyzer"
3. Click "Setup Sheet Headers" to create the column headers
4. The sheet will be formatted with headers and styling

### Analyzing Invoices

1. Click "Invoice Extractor AI" → "Open Invoice Analyzer"
2. Paste invoice text in the textarea
3. Click "Analyze Invoice"
4. The extracted data will be inserted as a new row

## Troubleshooting

### Menu Not Appearing
- Run the `onOpen` function manually in Apps Script
- Refresh the Google Sheets page
- Check browser console for JavaScript errors

### API Calls Failing
- Verify the backend URL is correct in `Code.gs`
- Ensure the backend is running and accessible
- Check CORS configuration on the backend

### Data Not Inserting
- Check Google Sheets permissions
- Verify the sheet is not protected
- Run "Setup Sheet Headers" first

## Sample Invoice Text

Use this sample text to test the add-on:

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

## File Structure

```
frontend/
├── Code.gs              # Main Apps Script file
├── Sidebar.html         # HTML sidebar interface
└── README.md            # This file
```

## Configuration

### Backend URL
Update the `BACKEND_URL` in `Code.gs`:
```javascript
const BACKEND_URL = 'https://your-backend-url.com';
```

### API Endpoint
The default endpoint is `/analyze-invoice`. If you change it in the backend, update it here:
```javascript
const API_ENDPOINT = '/analyze-invoice';
```

## Security Notes

- The add-on requires access to Google Sheets
- API calls are made from Google's servers
- No sensitive data is stored in the Apps Script
- All communication is over HTTPS

## Support

For issues:
1. Check the troubleshooting section
2. Verify backend URL and connectivity
3. Test with the sample invoice text
4. Check Google Sheets permissions 