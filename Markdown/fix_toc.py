import re

file_path = r'd:\Template\Markdown\DOC.md'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('<div style="font-size:2em;font-weight:bold;text-align:center;margin-bottom:10px">目录</div>')
end_idx = text.find('<div style="page-break-after:always;"></div>')

if start_idx != -1 and end_idx != -1:
    toc_text = text[start_idx:end_idx]
    
    items = []
    for line in toc_text.split('\n'):
        line = line.strip()
        if not line:
            continue
        m = re.match(r'\*\*(.*?)\s*[·\.]{2,}\s*(\d+)\*\*', line)
        if m:
            items.append((m.group(1).strip(), m.group(2).strip()))
    
    if len(items) > 0:
        new_toc_lines = []
        new_toc_lines.append('<div style="font-size:2em;font-weight:bold;text-align:center;margin-bottom:10px">目录</div>\n')
        new_toc_lines.append('<style>')
        new_toc_lines.append('.toc-item {')
        new_toc_lines.append('    display: flex;')
        new_toc_lines.append('    align-items: baseline;')
        new_toc_lines.append('    margin-bottom: 8px;')
        new_toc_lines.append('}')
        new_toc_lines.append('.toc-title {')
        new_toc_lines.append('    font-weight: bold;')
        new_toc_lines.append('}')
        new_toc_lines.append('.toc-dots {')
        new_toc_lines.append('    flex-grow: 1;')
        new_toc_lines.append('    border-bottom: 2px dotted #000;')
        new_toc_lines.append('    margin: 0 10px;')
        new_toc_lines.append('}')
        new_toc_lines.append('.toc-page {')
        new_toc_lines.append('    font-weight: bold;')
        new_toc_lines.append('}')
        new_toc_lines.append('</style>\n')
        
        for name, page in items:
            new_toc_lines.append(f'<div class="toc-item"><span class="toc-title">{name}</span><span class="toc-dots"></span><span class="toc-page">{page}</span></div>')
        
        new_toc_lines.append('\n')
        
        new_text = text[:start_idx] + '\n'.join(new_toc_lines) + text[end_idx:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Successfully updated DOC.md")
    else:
        print("No TOC items found")
else:
    print("Could not find TOC start or end tags")
