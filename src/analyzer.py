def analyze_features(records: list) -> list:
    """
    Identifies heat factors (high temp, low vegetation, high density)
    for each area record.
    """
    print("Analyzing features...")
    analyzed_data = []
    for record in records:
        analysis = record.copy()
        
        # Detect feature conditions based on thresholds to assist agent reasoning
        analysis['is_high_temp'] = record['temperature'] > 34
        analysis['is_very_high_temp'] = record['temperature'] > 38
        analysis['is_low_vegetation'] = record['tree_coverage'] < 20
        analysis['is_high_density'] = record['building_density'] > 70
        
        analyzed_data.append(analysis)
        
    return analyzed_data
