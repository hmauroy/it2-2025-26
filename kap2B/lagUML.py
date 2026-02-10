#!/usr/bin/env python3
"""
Script som genererer HTML med UML-klassediagram fra en Python-fil.
Bruk: python lagUML.py <python_fil>

Author: Claude 4.5 Sonnet.
Prompter: Henrik C. Mauroy
"""

import ast
import sys
import os

def parse_python_file(filename):
    """Parser en Python-fil og returnerer klassedata."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tree = ast.parse(content)
    
    # Finn første klassedefinisjon
    class_def = None
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_def = node
            break
    
    if not class_def:
        print(f"Feil: Ingen klassedefinisjon funnet i {filename}")
        sys.exit(1)
    
    # Hent klassenavn
    class_name = class_def.name
    
    # Hent parent class (arv)
    parent = None
    if class_def.bases:
        if isinstance(class_def.bases[0], ast.Name):
            parent = class_def.bases[0].id
        elif isinstance(class_def.bases[0], ast.Attribute):
            parent = class_def.bases[0].attr
    
    # Hent attributter fra __init__
    attributes = []
    methods = []
    
    for item in class_def.body:
        if isinstance(item, ast.FunctionDef):
            method_name = item.name
            
            # Hent parametere (unntatt self)
            params = []
            for arg in item.args.args:
                if arg.arg != 'self':
                    params.append(arg.arg)
            params_str = ', '.join(params)
            
            # Sjekk returtype (hvis tilgjengelig)
            return_type = "None"
            if item.returns:
                if isinstance(item.returns, ast.Name):
                    return_type = item.returns.id
                elif isinstance(item.returns, ast.Constant):
                    return_type = str(item.returns.value)
            
            methods.append({
                'name': method_name,
                'params': params_str,
                'returnType': return_type
            })
            
            # Hent attributter fra __init__
            if method_name == '__init__':
                for node in ast.walk(item):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Attribute):
                                if isinstance(target.value, ast.Name) and target.value.id == 'self':
                                    attr_name = target.attr
                                    
                                    # Prøv å gjette type
                                    attr_type = guess_type(node.value)
                                    
                                    attributes.append({
                                        'name': attr_name,
                                        'type': attr_type
                                    })
    
    return {
        'name': class_name,
        'parent': parent,
        'attributes': attributes,
        'methods': methods
    }

def guess_type(node):
    """Gjetter typen basert på AST-noden."""
    if isinstance(node, ast.Constant):
        value = node.value
        if isinstance(value, bool):
            return 'bool'
        elif isinstance(value, int):
            return 'int'
        elif isinstance(value, float):
            return 'float'
        elif isinstance(value, str):
            return 'str'
    elif isinstance(node, ast.List):
        return 'list'
    elif isinstance(node, ast.Dict):
        return 'dict'
    elif isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name):
            return node.func.id
    return 'Any'

def generate_html(class_data, output_file):
    """Genererer HTML-fil med UML-diagram."""
    
    html_template = """<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UML Klassediagram - {class_name}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        
        .container {{
            background: white;
            border-radius: 10px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 30px;
            max-width: 600px;
        }}
        
        .uml-class {{
            border: 2px solid #333;
            border-radius: 8px;
            overflow: hidden;
            background: #fff;
        }}
        
        .class-name {{
            background: #4a5568;
            color: white;
            padding: 15px;
            text-align: center;
            font-weight: bold;
            font-size: 1.3em;
        }}
        
        .inheritance {{
            background: #e2e8f0;
            padding: 8px 15px;
            text-align: center;
            font-style: italic;
            color: #4a5568;
            border-bottom: 1px solid #cbd5e0;
        }}
        
        .section {{
            padding: 15px;
            border-bottom: 2px solid #333;
        }}
        
        .section:last-child {{
            border-bottom: none;
        }}
        
        .section-title {{
            font-weight: bold;
            color: #2d3748;
            margin-bottom: 10px;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        .attribute, .method {{
            padding: 5px 0;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            line-height: 1.6;
            color: #1a202c;
        }}
        
        .type {{
            color: #3182ce;
        }}
        
        h1 {{
            color: white;
            text-align: center;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>UML Klassediagram</h1>
        <div id="umlDiagram"></div>
    </div>

    <script>
        const classData = {class_data_json};

        function generateUML(data) {{
            const diagram = document.getElementById('umlDiagram');
            
            let html = '<div class="uml-class">';
            
            html += `<div class="class-name">${{data.name}}</div>`;
            
            if (data.parent) {{
                html += `<div class="inheritance">utvider ${{data.parent}}</div>`;
            }}
            
            if (data.attributes && data.attributes.length > 0) {{
                html += '<div class="section">';
                html += '<div class="section-title">Attributter</div>';
                data.attributes.forEach(attr => {{
                    html += `<div class="attribute">
                        ${{attr.name}}: <span class="type">${{attr.type}}</span>
                    </div>`;
                }});
                html += '</div>';
            }}
            
            if (data.methods && data.methods.length > 0) {{
                html += '<div class="section">';
                html += '<div class="section-title">Metoder</div>';
                data.methods.forEach(method => {{
                    const params = method.params ? `(${{method.params}})` : '()';
                    html += `<div class="method">
                        ${{method.name}}${{params}}: <span class="type">${{method.returnType}}</span>
                    </div>`;
                }});
                html += '</div>';
            }}
            
            html += '</div>';
            
            diagram.innerHTML = html;
        }}

        generateUML(classData);
    </script>
</body>
</html>"""
    
    # Konverter class_data til JSON
    import json
    class_data_json = json.dumps(class_data, indent=4, ensure_ascii=False)
    
    # Fyll inn template
    html_content = html_template.format(
        class_name=class_data['name'],
        class_data_json=class_data_json
    )
    
    # Skriv til fil
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"UML-diagram generert: {output_file}")

def main():
    if len(sys.argv) != 2:
        print("Bruk: python lagUML.py <python_fil>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"Feil: Filen {input_file} finnes ikke")
        sys.exit(1)
    
    # Parse Python-filen
    class_data = parse_python_file(input_file)
    
    # Generer output-filnavn
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = f"{base_name}_UML.html"
    
    # Generer HTML
    generate_html(class_data, output_file)

if __name__ == '__main__':
    main()