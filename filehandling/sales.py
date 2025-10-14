def read_complete_text(file_path):
    """Read and display complete file text with statistics"""
    with open(file_path) as f:
        txt = f.read()
        print("=== COMPLETE TEXT ===")
        print(f"length: {len(txt)} characters")
        print("=" * 50)
        return txt

def read_lines_info(file_path):
    """Read and display line information"""
    with open(file_path) as f:
        lines = f.readlines()
        print("=== ALL LINES INFO ===")
        print(f"no of lines in file: {len(lines)} lines")
        return lines

def process_lines(lines):
    """Process each line individually"""
    print("=== PROCESSING LINE BY LINE ===")
    for line in lines:
        print(line.strip())
    return lines

def extracting_products(file_path):

    print("=== EXTRACTING PRODUCTS WITH REGIONS ===") 
    products_data = []
    current_product = {}
    
    with open(file_path) as file:
        for line in file:
            line = line.strip()
            
            if line.startswith("Region:"):
                current_product['region'] = line.split(":")[1].strip()
            elif line.startswith("Product:"):
                current_product['name'] = line.split(":")[1].strip()
                products_data.append(current_product.copy())  # Use copy to avoid reference issues
                current_product = {}  # Reset for next product
    
    print("Products with regions:")
    for product in products_data:
        print(f"  {product['name']} - {product['region']}")
    
    return products_data

def extracting_products(file_path):
    print("===EXTRACTING PRODUCT NAMES===") 
    product_list=[]
    regoin_list=[]
    units_list=[]
    with open(file_path) as file:
        for line in file:
            if line.startswith("Region:"):
                #extract product name from line and append into list
                regoin_list.append(line.split(":")[1].strip())
            elif line.startswith("Product:"):
                product_list.append(line.split(":")[1].strip())
            elif line.startswith("Units"):
                units_list.append(line.split(":")[1].strip())

    print(product_list)
    print(regoin_list)
    print(units_list)

def all_records(file_path):
    records = []
    current_record = {}

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line.startswith("Region:"):
                current_region = line.split(":")[1].strip()
            elif line.startswith("Product:"):
                current_record["Region"] = current_region
                current_record["Product"] = line.split(":")[1].strip()
            elif line.startswith("Units Sold:"):
                current_record["Units Sold"] = int(line.split(":")[1].strip())
            elif line.startswith("Revenue:"):
                rev = line.split(":")[1].strip().replace(",", "").replace("$","")
                current_record["Revenue"] = int(rev)
            elif line.startswith("Salesperson:"):
                current_record["Salesperson"] = line.split(":")[1].strip()
                records.append(current_record)
                current_record = {}
    return records

def total_regions_from_records(records):
    print("=== UNIQUE REGIONS ANALYSIS ===")
    regions_set = set()
    products_set = set()
    
    for record in records:
        if "Region" in record:
            regions_set.add(record["Region"])
        if "Product" in record:
            products_set.add(record["Product"])
    
    print(f"Unique sales regions: {regions_set}")
    print(f"Unique products: {products_set}")
    return regions_set

def duplicate_records_from_records(records):
    print("=== DUPLICATE RECORDS CHECK ===")
    duplicate = []
    seen = set()
    
    for record in records:
        values = tuple(record.values())   # Convert to tuple for hashing
        if values in seen:
            duplicate.append(record)
        else:
            seen.add(values)
    
    print(f"Found {len(duplicate)} duplicate records:")
    for dup in duplicate:
        print(f"  - {dup['Product']} in {dup['Region']} by {dup['Salesperson']}")
    
    return duplicate

def sales_report(file_path):
    print("=== SALES REPORT GENERATION ===")
    records = all_records(file_path)
    performance = {}
    for record in records:
         person = record['Salesperson']
         if person not in performance:
             performance[person] = {
                 "region": set(),
                 "total_revenue": 0,
                 "total_units": 0,
                 "products_sold": []
             }
         performance[person]["region"].add(record['Region'])
         performance[person]["total_revenue"] += record["Revenue"]
         performance[person]["total_units"] += record["Units Sold"]
         performance[person]['products_sold'].append(record['Product'])
    return performance
  
def salesperson_report(file_path, name):
    sales_persons = sales_report(file_path)
    found = False
    for person, sales in sales_persons.items():
        if name.lower() in person.lower():
            print(f"\n=== SALES REPORT FOR: {person} ===")
            print("=" * 40)
            print(f"Regions: {', '.join(sales['region'])}")
            print(f"Total Revenue: ${sales['total_revenue']:,}")
            print(f"Total Units Sold: {sales['total_units']}")
            print(f"Products Sold: {', '.join(sales['products_sold'])}")
            found = True
            break
    
    if not found:
        print(f"❌ Salesperson '{name}' not found. Available salespeople:")
        for person in sales_persons.keys():
            print(f"  - {person}")

def high_value_products(file_path, min_revenue=10000):
     print("=== HIGH VALUE PRODUCTS ANALYSIS ===")
     products=[]
     data=all_records(file_path)
     for record in data:
         if record["Revenue"]>=min_revenue:
             products.append(record)
     for product in products:
        print(f"  - {product['Product']}: ${product['Revenue']:,} in {product['Region']}")

def rank_salespersons(file_path):
    print("======SORTING SALES PERSONS=====")
    sales_persons = sales_report(file_path)  #dict
    print(sales_persons)
    print("sorting based on name")
    sorted_sales=sorted(sales_persons)
    print(sorted_sales)
    print("sorting based on revenue")
    print(sorted(sales_persons.items(),key=lambda x : x[1]["total_revenue"],reverse=True))


def main():
    file_path = r"D:\Program Collection\Python\filehandling\files\sales_report.txt"
    
    try:
        print("="*50)
        print("=== SALES DATA ANALYSIS SYSTEM ===")
        print("="*50)
        
    
        complete_text = read_complete_text(file_path)
        lines = read_lines_info(file_path)
        process_lines(lines)
        
      
        products_data = extracting_products(file_path)

        records = all_records(file_path)
        print(records)
        total_regions_from_records(records)
        duplicate_records_from_records(records)
        print("="*50)
        high_value_products(file_path, min_revenue=10000)
        
       
        sales_report_data = sales_report(file_path)
        print("="*50)
        rank_salespersons(file_path)
        print("="*50)
        person = input("Enter sales person name: ")
        salesperson_report(file_path, person)

        
        print("\n" + "="*50)
        print("=== ANALYSIS COMPLETE ===")
        print("="*50)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied: {file_path}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()