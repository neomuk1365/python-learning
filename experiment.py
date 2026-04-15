header = f"{'CITY':<15} | {'COUNTRY':<10} | {'POPULATION':<12} | {'FACT'}"
print(header)
print("-" * len(header))
# FAANG Style: Clean, Scalable, and Professional
cities = {
    'kolkata': {
        'country': 'India',
        'population': '1.5cr',
        'fact': 'Cultural capital of India'
    },
    # ... other cities
}

# 1. Define a template for consistent output
header = f"{'CITY':<15} | {'COUNTRY':<10} | {'POPULATION':<12} | {'FACT'}"
print(header)
print("-" * len(header))

# 2. Iterate using unpacking for speed and readability
for city, info in cities.items():
    country = info.get('country', 'N/A')
    pop = info.get('population', 'N/A')
    fact = info.get('fact', 'N/A')
    
    print(f"{city.title():<15} | {country:<10} | {pop:<12} | {fact}")