import sys
from src.loader import load_data
from src.processor import process_data
from src.analyzer import analyze_features
from src.agent import run_agent
from src.reporter import generate_report

def main():
    print("Starting UHI Analysis Agent...")
    
    # 1. Data Ingestion
    data_path = 'data/data.csv'
    try:
        df = load_data(data_path)
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)
        
    # 2. Data Processing
    records = process_data(df)
    
    # 3. Feature Analysis
    analyzed_data = analyze_features(records)
    
    # 4. AI Agent Reasoning
    results = run_agent(analyzed_data)
    
    # 5. Report Generation
    generate_report(results)
    
    print("Agent execution completed successfully.")

if __name__ == "__main__":
    main()
