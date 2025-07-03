
import sys
import os
import webview

class Api:
    def execute_script(self, code):
        try:
            exec(code)
            return 'Script executed successfully'
        except Exception as e:
            return f'Error: {str(e)}'

def main():
    if len(sys.argv) != 2:
        print("Usage: python viewer.py <svg_file>")
        sys.exit(1)

    svg_path = os.path.abspath(sys.argv[1])
    
    if not os.path.exists(svg_path):
        print(f"File {svg_path} not found")
        sys.exit(1)

    api = Api()
    window = webview.create_window(
        'SVG Viewer', 
        url=f'file://{svg_path}',
        js_api=api,
        width=800,
        height=600
    )
    webview.start()

if __name__ == '__main__':
    main()
