from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')

@app.route('/api/matches', methods=['GET'])
def get_matches():
    headers = {
        'X-Auth-Token': API_KEY
    }
    
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Process the matches data
        matches = []
        for match in data.get('matches', []):
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            utc_date = match['utcDate']
            
            # Convert UTC date to local time (optional)
            match_date = datetime.fromisoformat(utc_date.replace('Z', '+00:00'))
            
            matches.append({
                'homeTeam': home_team,
                'awayTeam': away_team,
                'date': match_date.strftime('%Y-%m-%d %H:%M')
            })
        
        return jsonify({'matches': matches})
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)