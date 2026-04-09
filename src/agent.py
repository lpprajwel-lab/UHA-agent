import os

def run_agent(analyzed_records: list) -> list:
    """
    Core AI Agent decision-making.
    Follows Input -> Reasoning -> Action -> Output pattern.
    """
    print("Running agent...")
    results = []
    
    # Check for API key to see if LLM is available
    api_key = os.environ.get("GEMINI_API_KEY")
    use_llm = api_key is not None
    
    if use_llm:
        print("Optional LLM API key detected... For fully fleshed models, use API.")

    for record in analyzed_records:
        temp = record['temperature']
        tree = record['tree_coverage']
        density = record['building_density']
        area = record['area']
        
        # Rule-based Reasoning (as requested)
        risk_level = "Low"
        reasoning = []
        solutions = []
        impact = ""
        
        if temp > 38 and tree < 20:
            risk_level = "High"
            reason = "Low tree coverage and high building density trap heat" if density > 70 else "Temperature is critically high and vegetation is too low."
            solutions = ["Increase tree plantation", "Install cool roofs", "Implement green infrastructure"]
            impact = "Expected 2-4°C reduction"
            
        elif temp > 34:
            risk_level = "Medium"
            reason = "Elevated temperatures"
            if tree < 30:
                reason += " combined with a moderate lack of tree coverage contributes to heat"
            solutions = ["Add street trees", "Use reflective pavements", "Install cool roofs"]
            impact = "Expected 1-2°C reduction"
            
        else:
            risk_level = "Low"
            reason = "Temperature falls within safe parameters with relatively sufficient vegetation or low density."
            solutions = ["Maintain current green spaces", "Monitor future developments"]
            impact = "Expected 0-1°C reduction"
            
        # Agent's Output Action
        result = {
            "area": area,
            "risk_level": risk_level,
            "reason": reason,
            "solutions": solutions,
            "impact": impact,
            "temp_context": temp,
            "tree_context": tree,
            "density_context": density
        }
        
        results.append(result)
        
    return results
