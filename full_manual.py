import os

files = [
    'index.html',
    'pages/01_Introduction.html',
    'pages/02_Installation.html',
    'pages/03_GettingStarted.html',
    'pages/04_Interface.html',
    'pages/05_AircraftOps.html',
    'pages/06_Weather_&_Time.html',
    'pages/07_Special_Showcase.html',
    'pages/08_VFX_&_Fun.html',
    'pages/09_Help_&_Support.html',
    'pages/10_Acknowledgements.html'
]

output_file = 'full_manual.html'

def generate_full_manual():
    sidebar_html = """<div class="sidebar">
    <h3>Simulator Menu</h3>
    <a href="./index.html">00. Index/Dashboard</a>
    <a href="pages/01_Introduction.html">01. Introduction</a>
    <a href="pages/02_Installation.html">02. Installation</a>
    <a href="pages/03_GettingStarted.html">03. Getting Started</a>
    <a href="pages/04_Interface.html">04. Interface</a>
    <a href="pages/05_AircraftOps.html">05. Aircraft Ops</a>
    <a href="pages/06_Weather_&_Time.html">06. Weather & Time</a>
    <a href="pages/07_Special_Showcase.html">07. Special Showcase</a>
    <a href="pages/08_VFX_&_Fun.html">08. VFX & Fun</a>
    <a href="pages/09_Help_&_Support.html">09. Help & Support</a>
    <a href="pages/10_Acknowledgements.html">10. Acknowledgements</a>
    <a href="./full_manual.html">99. Print Full Manual</a>
</div>"""

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
        outfile.write('<meta charset="UTF-8">\n<title>BAF ATC Simulator Operation Manual</title>\n')
        outfile.write('<link rel="stylesheet" href="style.css">\n')
        
        # CSS Update: We add page-break-after to the container itself
        # This removes the need for a separate blank div that causes the empty page
        outfile.write('<style>\n.page-container { page-break-after: always; margin-bottom: 20px; }\n@media print { .sidebar { display: none; } }\n</style>\n')
        outfile.write('</head>\n<body>\n')
        
        outfile.write(sidebar_html + '\n\n')

        for file_name in files:
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    content = content.replace('src="../Images/', 'src="Images/')
                    
                    start_tag = '<div class="page-container">'
                    start_idx = content.find(start_tag)
                    
                    if start_idx != -1:
                        # Extract from the start tag
                        content_after_start = content[start_idx:]
                        # Find the matching closing div
                        end_idx = content_after_start.rfind('</div>')
                        
                        if end_idx != -1:
                            page_content = content_after_start[:end_idx + 6]
                            # Write directly, no extra div needed
                            outfile.write(page_content + '\n')
            else:
                print(f"Warning: {file_name} not found.")

        outfile.write('\n</body>\n</html>')

if __name__ == "__main__":
    generate_full_manual()
    print("full_manual.html has been generated.")