import os
import json
import logging
from typing import Optional
from openai import OpenAI
from models import InvoiceData


class InvoiceAnalyzer:
    """AI-powered invoice analysis using OpenAI GPT-4"""
    
    def __init__(self):
        """Initialize the OpenAI client"""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        
        self.client = OpenAI(api_key=api_key)
        self.logger = logging.getLogger(__name__)
    
    async def analyze_invoice(self, text: str) -> InvoiceData:
        """
        Analyze invoice text using OpenAI GPT-4
        
        Args:
            text (str): Raw invoice text
            
        Returns:
            InvoiceData: Extracted invoice information
        """
        try:
            # Prepare the prompt for GPT-4
            system_prompt = """
            You are an expert invoice analyzer. Extract the following information from the invoice text:
            - invoice_id: The invoice number or ID
            - vendor: The company or vendor name
            - total: The total amount (as a number, no currency symbols)
            - date: The invoice date (in YYYY-MM-DD format)
            
            Return ONLY a valid JSON object with these fields. If a field cannot be found, use null.
            Example: {"invoice_id": "INV-001", "vendor": "ABC Company", "total": 150.00, "date": "2024-01-15"}
            """
            
            user_prompt = f"Please analyze this invoice text and extract the required information:\n\n{text}"
            
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.1,  # Low temperature for consistent results
                max_tokens=500
            )
            
            # Extract the response content
            content = response.choices[0].message.content.strip()
            
            # Parse JSON response
            try:
                # Clean the response in case it contains markdown formatting
                if content.startswith("```json"):
                    content = content[7:]
                if content.endswith("```"):
                    content = content[:-3]
                
                parsed_data = json.loads(content.strip())
                
                # Create InvoiceData object
                invoice_data = InvoiceData(
                    invoice_id=parsed_data.get("invoice_id"),
                    vendor=parsed_data.get("vendor"),
                    total=parsed_data.get("total"),
                    date=parsed_data.get("date")
                )
                
                self.logger.info(f"Successfully analyzed invoice: {invoice_data}")
                return invoice_data
                
            except json.JSONDecodeError as e:
                self.logger.error(f"Failed to parse JSON response: {e}")
                self.logger.error(f"Raw response: {content}")
                raise ValueError(f"Invalid JSON response from AI: {content}")
                
        except Exception as e:
            self.logger.error(f"Error analyzing invoice: {str(e)}")
            raise e 