import os
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from models import InvoiceAnalysisRequest, InvoiceAnalysisResponse
from ai_invoice import InvoiceAnalyzer

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Invoice Extractor AI",
    description="AI-powered invoice analysis API",
    version="1.0.0"
)

# Add CORS middleware for Google Apps Script
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the invoice analyzer
try:
    invoice_analyzer = InvoiceAnalyzer()
    logger.info("Invoice analyzer initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize invoice analyzer: {e}")
    invoice_analyzer = None


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Invoice Extractor AI API",
        "status": "running",
        "version": "1.0.0"
    }


@app.post("/analyze-invoice", response_model=InvoiceAnalysisResponse)
async def analyze_invoice(request: InvoiceAnalysisRequest):
    """
    Analyze invoice text and extract structured data
    
    Args:
        request (InvoiceAnalysisRequest): Request containing invoice text
        
    Returns:
        InvoiceAnalysisResponse: Extracted invoice data or error information
    """
    try:
        # Validate input
        if not request.text or not request.text.strip():
            raise HTTPException(
                status_code=400,
                detail="Invoice text is required and cannot be empty"
            )
        
        # Check if analyzer is available
        if invoice_analyzer is None:
            raise HTTPException(
                status_code=500,
                detail="Invoice analyzer is not available"
            )
        
        logger.info(f"Analyzing invoice text (length: {len(request.text)})")
        
        # Analyze the invoice
        invoice_data = await invoice_analyzer.analyze_invoice(request.text)
        
        # Create response
        response = InvoiceAnalysisResponse(
            invoice_id=invoice_data.invoice_id,
            vendor=invoice_data.vendor,
            total=invoice_data.total,
            date=invoice_data.date,
            success=True
        )
        
        logger.info(f"Successfully analyzed invoice: {response}")
        return response
        
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except ValueError as e:
        # Handle validation errors
        logger.error(f"Validation error: {e}")
        return InvoiceAnalysisResponse(
            success=False,
            error_message=str(e)
        )
    except Exception as e:
        # Handle unexpected errors
        logger.error(f"Unexpected error analyzing invoice: {e}")
        return InvoiceAnalysisResponse(
            success=False,
            error_message="An unexpected error occurred while analyzing the invoice"
        )


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "analyzer_available": invoice_analyzer is not None
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    ) 