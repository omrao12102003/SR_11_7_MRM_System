from flask import Flask, jsonify, request, send_from_directory, Response
from services.governance import load_models, load_approvals, log_action
from services.report_builder import build_summary
import os

app = Flask(__name__, static_folder='../frontend')

@app.route('/api/models')
def api_models():
    return jsonify(load_models())

@app.route('/api/approvals') 
def api_approvals():
    return jsonify(load_approvals())

@app.route('/api/report')
def api_report():
    return Response(build_summary(), mimetype='text/plain')

@app.route('/api/upload', methods=['POST'])
def api_upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    path = f"storage/uploads/{file.filename}"
    os.makedirs("storage/uploads", exist_ok=True)
    file.save(path)
    log_action('faculty', 'UPLOAD', file.filename, 'Phase 5 audit')
    return jsonify({'status': 'uploaded'})

@app.route('/')
@app.route('/<path:path>')
def frontend(path='index.html'):
    return send_from_directory('../frontend', path)

if __name__ == '__main__':
    print("🚀 Phase 5 Server: http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
