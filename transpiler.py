import re

class PythonToJavaJavaScriptTranspiler:
    def __init__(self, python_code):
        self.python_code = python_code

    def transpile_to_java(self):
        java_code = self.convert_classes_to_java(self.python_code)
        java_code = self.convert_function_signature_to_java(java_code)
        java_code = self.convert_function_body_to_java(java_code)
        java_code = self.convert_print_statements_to_java(java_code)
        return java_code

    def transpile_to_javascript(self):
        js_code = self.convert_classes_to_javascript(self.python_code)
        js_code = self.convert_function_signature_to_javascript(js_code)
        js_code = self.convert_function_body_to_javascript(js_code)
        js_code = self.convert_print_statements_to_javascript(js_code)
        return js_code

    def convert_classes_to_java(self, code):
        # Convert class definitions
        code = re.sub(r'class\s+(\w+):', r'public class \1 {', code)
        code = re.sub(r'\s*def\s+__init__\s*\(self, (.*?)\):', r'public \1() {', code)
        return code

    def convert_classes_to_javascript(self, code):
        # Convert class definitions
        code = re.sub(r'class\s+(\w+):', r'class \1 {', code)
        code = re.sub(r'\s*def\s+__init__\s*\(self, (.*?)\):', r'constructor(\1) {', code)
        return code

    def convert_function_signature_to_java(self, code):
        pattern = r'def\s+(\w+)\s*\((.*?)\)\s*:'
        # Replace all function definitions, not just the first
        def repl(match):
            function_name = match.group(1)
            params = match.group(2)
            java_params = []
            if params:
                param_list = [param.strip() for param in params.split(',')]
                for param in param_list:
                    param_type = "int" if "int" in param else "double" if "float" in param else "String" if "str" in param else "Object"
                    java_params.append(f"{param_type} {param.split(':')[0].strip()}")
            java_param_str = ', '.join(java_params)
            return f"public Object {function_name}({java_param_str}) {{"
        java_code = re.sub(pattern, repl, code)
        return java_code

    def convert_function_body_to_java(self, code):
        lines = code.split('\n')
        converted_lines = []

        for line in lines:
            line = self.convert_control_structures_to_java(line)

            # Ensure variable declarations and semicolons
            if '=' in line and not line.strip().startswith('return'):
                var_name = line.split('=')[0].strip()
                line = f"int {line.strip()};"  # Assuming int for all variables

            elif line.strip().startswith('return'):
                line = line.strip() + ';'

            converted_lines.append(line.strip())

        converted_lines.append('}')  # Add closing brace for the Java function
        return '\n'.join(converted_lines)

    def convert_function_signature_to_javascript(self, code):
        pattern = r'def\s+(\w+)\s*\((.*?)\)\s*:'
        # Replace all function definitions, not just the first
        def repl(match):
            function_name = match.group(1)
            params = match.group(2)
            js_params = []
            if params:
                param_list = [param.strip() for param in params.split(',')]
                for param in param_list:
                    js_params.append(param)
            js_param_str = ', '.join(js_params)
            return f"function {function_name}({js_param_str}) {{"
        js_code = re.sub(pattern, repl, code)
        return js_code

    def convert_function_body_to_javascript(self, code):
        lines = code.split('\n')
        converted_lines = []

        for line in lines:
            line = self.convert_control_structures_to_javascript(line)

            if '=' in line and not line.strip().startswith('return'):
                line = f"let {line.strip()};"  # Declare with let

            elif line.strip().startswith('return'):
                line = line.strip() + ';'

            converted_lines.append(line.strip())

        converted_lines.append('}')  # Add closing brace for the JS function
        return '\n'.join(converted_lines)

    def convert_control_structures_to_java(self, line):
        # Convert if statements
        line = re.sub(r'if\s*\((.*?)\)\s*:', r'if (\1) {', line)
        line = re.sub(r'elif\s*\((.*?)\)\s*:', r'else if (\1) {', line)
        line = re.sub(r'else\s*:', r'else {', line)
        
        # Convert for loops
        line = re.sub(r'for\s+(\w+)\s+in\s+(\w+):', r'for (int \1 : \2) {', line)

        # Convert while loops
        line = re.sub(r'while\s*\((.*?)\)\s*:', r'while (\1) {', line)

        # Convert try-except
        line = re.sub(r'try\s*:', r'try {', line)
        line = re.sub(r'except\s*:\s*', r'catch (Exception e) {', line)

        return line

    def convert_control_structures_to_javascript(self, line):
        # Convert if statements
        line = re.sub(r'if\s*\((.*?)\)\s*:', r'if (\1) {', line)
        line = re.sub(r'elif\s*\((.*?)\)\s*:', r'else if (\1) {', line)
        line = re.sub(r'else\s*:', r'else {', line)
        
        # Convert for loops
        line = re.sub(r'for\s+(\w+)\s+in\s+(\w+):', r'for (let \1 of \2) {', line)

        # Convert while loops
        line = re.sub(r'while\s*\((.*?)\)\s*:', r'while (\1) {', line)

        # Convert try-catch
        line = re.sub(r'try\s*:', r'try {', line)
        line = re.sub(r'except\s*:\s*', r'catch (e) {', line)

        return line

    def convert_print_statements_to_java(self, code):
        # Convert Python print statements to Java System.out.println
        code = re.sub(r'print\((.*?)\)', r'System.out.println(\1);', code)
        return code

    def convert_print_statements_to_javascript(self, code):
        # Convert Python print statements to JavaScript console.log
        code = re.sub(r'print\((.*?)\)', r'console.log(\1);', code)
        return code

    def convert_lists_to_java(self, line):
        # Convert Python lists to Java arrays
        line = re.sub(r'(\w+)\s*=\s*\[(.*?)\]', r'\1[] = new int[]{\2};', line)
        return line

    def convert_lists_to_javascript(self, line):
        # Convert Python lists to JavaScript arrays
        line = re.sub(r'(\w+)\s*=\s*\[(.*?)\]', r'\1 = [\2];', line)
        return line

# Example usage:
python_code = """
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(result)
        print(result)
        return result

    def divide(self, a, b):
        try:
            print(a / b)
            return a / b
        except ZeroDivisionError:
            print('Cannot divide by zero')
            return 'Cannot divide by zero'
"""

transpiler = PythonToJavaJavaScriptTranspiler(python_code)
java_output = transpiler.transpile_to_java()
js_output = transpiler.transpile_to_javascript()

print("Java Output:\n", java_output)
print("JavaScript Output:\n", js_output)
