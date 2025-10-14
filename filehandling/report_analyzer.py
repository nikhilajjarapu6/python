import pdfplumber
import re

def extract_cbc_from_text():
    """
    Extract CBC data directly from text when tables aren't detected
    """
    with pdfplumber.open("sample_blood_report.pdf") as pdf:
        page_1 = pdf.pages[0]
        text = page_1.extract_text()
        
        print("🩸 EXTRACTING CBC FROM TEXT")
        print("=" * 60)
        
        # Split into lines
        lines = text.split('\n')
        
        in_cbc_section = False
        cbc_data = []
        
        for line in lines:
            line = line.strip()
            
            # Find where CBC section starts
            if "Complete Blood Count" in line:
                in_cbc_section = True
                print("📍 Found CBC Section!")
                continue
                
            # Find where CBC section ends
            if "Total WBC and Differential Count" in line:
                in_cbc_section = False
                print("📍 Moving to WBC Section...")
                # Don't break - continue to get WBC data
                
            if in_cbc_section and line:
                # Skip empty lines and headers
                if not line or any(keyword in line for keyword in ['Test', 'Result', 'Unit', '---']):
                    continue
                    
                # This line might contain test data
                print(f"📄 Processing line: {line}")
                
                # Try to extract test name, value, unit, range
                # Pattern: "Test Name Value Unit Range"
                pattern1 = r'([A-Za-z\s]+)\s+([\d.]+)\s+([A-Za-z/%]+)\s+([\d.\s-]+)'
                pattern2 = r'([A-Za-z\s]+)\s+([\d.]+)\s+([\d.\s-]+)'
                
                match1 = re.search(pattern1, line)
                match2 = re.search(pattern2, line)
                
                if match1:
                    test_name = match1.group(1).strip()
                    value = match1.group(2).strip()
                    unit = match1.group(3).strip()
                    ref_range = match1.group(4).strip()
                    
                    cbc_data.append({
                        'test': test_name,
                        'value': value,
                        'unit': unit,
                        'range': ref_range
                    })
                    print(f"✅ Extracted: {test_name} = {value} {unit} ({ref_range})")
                    
                elif match2:
                    test_name = match2.group(1).strip()
                    value = match2.group(2).strip()
                    ref_range = match2.group(3).strip()
                    
                    cbc_data.append({
                        'test': test_name,
                        'value': value,
                        'unit': '',
                        'range': ref_range
                    })
                    print(f"✅ Extracted: {test_name} = {value} ({ref_range})")
        
        return cbc_data

# Run it
cbc_results = extract_cbc_from_text()

print("\n📋 FINAL CBC RESULTS:")
print("=" * 50)
for test in cbc_results:
    print(f"{test['test']:20} {test['value']:8} {test['unit']:10} {test['range']}")