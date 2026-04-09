def generate_report(results: list):
    """
    Formats and prints the results in a structured, readable format.
    """
    print("\n" + "="*50)
    print("URBAN HEAT ISLAND (UHI) ANALYSIS REPORT")
    print("="*50 + "\n")
    
    for result in results:
        print("-" * 40)
        print(f"Area: {result['area']}")
        print(f"Heat Risk: {result['risk_level']}")
        print(f"Reason: {result['reason']}")
        
        print("Solutions:")
        for solution in result['solutions']:
            print(f"  - {solution}")
            
        print(f"Impact: {result['impact']}")
        
    print("-" * 40)
    print()
