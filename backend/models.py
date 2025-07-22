from pydantic import BaseModel
from typing import Optional
from datetime import date


class InvoiceAnalysisRequest(BaseModel):
    """Request model for invoice analysis"""
    text: str


class InvoiceAnalysisResponse(BaseModel):
    """Response model for invoice analysis"""
    invoice_id: Optional[str] = None
    vendor: Optional[str] = None
    total: Optional[float] = None
    date: Optional[str] = None
    success: bool
    error_message: Optional[str] = None


class InvoiceData(BaseModel):
    """Internal model for extracted invoice data"""
    invoice_id: Optional[str] = None
    vendor: Optional[str] = None
    total: Optional[float] = None
    date: Optional[str] = None 