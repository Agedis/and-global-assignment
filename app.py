
import subprocess
import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_json():
    input_json = request.get_json()

    try:
        # Run the external Python script and pass the JSON data to its stdin
        process = subprocess.run(
            ['python', 'process.py'],
            input=json.dumps(input_json).encode('utf-8'),
            capture_output=True,
            check=True
        )

        # Get the processed JSON from the script's stdout
        processed_json = json.loads(process.stdout)
        return jsonify(processed_json)

    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Error in processing script", "details": e.stderr.decode()}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON output from processing script"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
