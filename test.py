from flask import Flask, render_template, request, jsonify
from nanonets import NANONETSOCR
from PIL import Image
import os

app = Flask(__name__)

# Initialize the OCR model
model = NANONETSOCR()
model.set_token('177e1419-fa27-11ee-8a88-16c7fbacd668')

@app.route('/')
def index():
    return render_template('options.html')

@app.route('/perform_ocr', methods=['POST'])
def perform_ocr():
    # Get the file from the request
    file = request.files['file']
    
    # Save the file temporarily
    file_path = 'temp.png'
    file.save(file_path)
    
    # Perform OCR on the image
    model.convert_to_csv(file_path, output_file_name='output.csv')
    
    # Delete the temporary file
    os.remove(file_path)
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)

