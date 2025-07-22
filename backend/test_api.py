#!/usr/bin/env python3
"""
Test script for Invoice Extractor AI API
"""

import requests
import json
import sys

# Configuration
API_BASE_URL = "http://localhost:8000"
TEST_INVOICE_TEXT = """
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
"""

def test_health_check():
    """Test the health check endpoint"""
    print("🔍 Testing health check...")
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Is the server running?")
        return False

def test_analyze_invoice():
    """Test the invoice analysis endpoint"""
    print("\n📄 Testing invoice analysis...")
    
    payload = {
        "text": TEST_INVOICE_TEXT
    }
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/analyze-invoice",
            headers={"Content-Type": "application/json"},
            json=payload
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Invoice analysis successful")
            print(f"   Invoice ID: {result.get('invoice_id')}")
            print(f"   Vendor: {result.get('vendor')}")
            print(f"   Total: {result.get('total')}")
            print(f"   Date: {result.get('date')}")
            print(f"   Success: {result.get('success')}")
            return True
        else:
            print(f"❌ Invoice analysis failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Is the server running?")
        return False
    except json.JSONDecodeError:
        print("❌ Invalid JSON response")
        return False

def test_empty_input():
    """Test with empty input"""
    print("\n🚫 Testing empty input validation...")
    
    payload = {
        "text": ""
    }
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/analyze-invoice",
            headers={"Content-Type": "application/json"},
            json=payload
        )
        
        if response.status_code == 400:
            print("✅ Empty input validation working correctly")
            return True
        else:
            print(f"❌ Empty input validation failed: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Is the server running?")
        return False

def main():
    """Run all tests"""
    print("🧪 Invoice Extractor AI - API Test Suite")
    print("=" * 50)
    
    tests = [
        test_health_check,
        test_analyze_invoice,
        test_empty_input
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! API is working correctly.")
        sys.exit(0)
    else:
        print("⚠️  Some tests failed. Please check the API configuration.")
        sys.exit(1)

if __name__ == "__main__":
    main() 