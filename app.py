from flask import Flask, render_template, request, jsonify
from transpiler import PythonToJavaJavaScriptTranspiler

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transpile', methods=['POST'])
def transpile():
    python_code = request.form.get('python_code', '')
    language = request.form.get('language', '')
    print("Received code:", python_code)
    print("Target language:", language)

    if not python_code.strip():
        return jsonify({'error': 'No Python code provided'}), 400

    transpiler = PythonToJavaJavaScriptTranspiler(python_code)

    try:
        if language == 'java':
            transpiled_code = transpiler.transpile_to_java()
        elif language == 'javascript':
            transpiled_code = transpiler.transpile_to_javascript()
        else:
            return jsonify({'error': 'Unsupported language'}), 400
        print("Transpiled code:", transpiled_code)
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)}), 400

    return jsonify({'transpiled_code': transpiled_code})

if __name__ == '__main__':
    app.run(debug=True)
