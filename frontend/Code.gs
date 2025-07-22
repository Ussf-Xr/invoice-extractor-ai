/**
 * Invoice Extractor AI - Google Apps Script
 * Main script file for the Google Sheets add-on
 */

// Configuration
const BACKEND_URL = 'https://your-backend-url.com'; // Replace with your deployed backend URL
const API_ENDPOINT = '/analyze-invoice';

/**
 * Creates a custom menu in Google Sheets
 */
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('Invoice Extractor AI')
    .addItem('Open Invoice Analyzer', 'showSidebar')
    .addToUi();
}

/**
 * Shows the sidebar with the invoice analyzer interface
 */
function showSidebar() {
  const html = HtmlService.createHtmlOutputFromFile('Sidebar')
    .setTitle('Invoice Extractor AI')
    .setWidth(400);
  SpreadsheetApp.getUi().showSidebar(html);
}

/**
 * Analyzes invoice text using the AI backend
 * @param {string} invoiceText - The raw invoice text to analyze
 * @returns {Object} The extracted invoice data
 */
function analyzeInvoice(invoiceText) {
  try {
    // Prepare the request payload
    const payload = {
      text: invoiceText
    };
    
    // Make the API call to the backend
    const response = UrlFetchApp.fetch(BACKEND_URL + API_ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      payload: JSON.stringify(payload),
      muteHttpExceptions: true
    });
    
    // Parse the response
    const responseCode = response.getResponseCode();
    const responseText = response.getContentText();
    
    if (responseCode !== 200) {
      throw new Error(`API request failed with status ${responseCode}: ${responseText}`);
    }
    
    const result = JSON.parse(responseText);
    
    // Check if the analysis was successful
    if (!result.success) {
      throw new Error(result.error_message || 'Analysis failed');
    }
    
    return {
      success: true,
      data: {
        invoice_id: result.invoice_id,
        vendor: result.vendor,
        total: result.total,
        date: result.date
      }
    };
    
  } catch (error) {
    console.error('Error analyzing invoice:', error);
    return {
      success: false,
      error: error.toString()
    };
  }
}

/**
 * Inserts the extracted invoice data into the active sheet
 * @param {Object} invoiceData - The extracted invoice data
 */
function insertInvoiceData(invoiceData) {
  try {
    const sheet = SpreadsheetApp.getActiveSheet();
    
    // Get the next empty row
    const lastRow = sheet.getLastRow();
    const nextRow = lastRow + 1;
    
    // Prepare the data row
    const rowData = [
      invoiceData.invoice_id || '',
      invoiceData.vendor || '',
      invoiceData.total || '',
      invoiceData.date || '',
      new Date() // Timestamp of when data was inserted
    ];
    
    // Insert the data
    sheet.getRange(nextRow, 1, 1, rowData.length).setValues([rowData]);
    
    // Auto-resize columns for better readability
    sheet.autoResizeColumns(1, rowData.length);
    
    return {
      success: true,
      message: 'Invoice data inserted successfully!'
    };
    
  } catch (error) {
    console.error('Error inserting invoice data:', error);
    return {
      success: false,
      error: error.toString()
    };
  }
}

/**
 * Sets up the sheet headers if they don't exist
 */
function setupSheetHeaders() {
  try {
    const sheet = SpreadsheetApp.getActiveSheet();
    
    // Check if headers already exist
    const firstRow = sheet.getRange(1, 1, 1, 5).getValues()[0];
    const hasHeaders = firstRow.some(cell => cell !== '');
    
    if (!hasHeaders) {
      // Set up headers
      const headers = ['Invoice ID', 'Vendor', 'Total', 'Date', 'Extracted At'];
      sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
      
      // Style the headers
      const headerRange = sheet.getRange(1, 1, 1, headers.length);
      headerRange.setFontWeight('bold');
      headerRange.setBackground('#4285f4');
      headerRange.setFontColor('white');
      
      // Freeze the header row
      sheet.setFrozenRows(1);
    }
    
    return { success: true };
    
  } catch (error) {
    console.error('Error setting up sheet headers:', error);
    return {
      success: false,
      error: error.toString()
    };
  }
} 