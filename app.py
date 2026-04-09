from flask import Flask, render_template, jsonify
# import the agent logic
from src.loader import load_data
from src.processor import process_data
from src.analyzer import analyze_features
from src.agent import run_agent

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def execute_agent():
    try:
        data_path = 'data/data.csv'
        df = load_data(data_path)
        records = process_data(df)
        analyzed_data = analyze_features(records)
        results = run_agent(analyzed_data)
        return jsonify({"status": "success", "data": results})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
