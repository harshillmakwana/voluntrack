import os
import re

directory = r'd:\Project\volunteer_project\volunteer_pro\templates\adminapp'
count = 0

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already updated
        if 'list_payments' in content:
            continue
            
        # Perform replacement for single quotes
        target_single = r'(<a class=["\']nav-item["\'] href=["\']\{\%\s*url\s+[\'"]list_Attendance[\'"]\s*\%\}\s*["\']\s*>\s*<\s*span\s+class=["\']icon["\']\s*>\s*✅\s*<\s*/span\s*>\s*Attended List\s*<\s*/a\s*>\s*)'
        
        new_content = re.sub(
            target_single, 
            r'\1\n\n<a class="nav-item" href="{% url \'list_payments\' %}"><span class="icon">💰</span>Payment List</a>\n', 
            content,
            flags=re.IGNORECASE
        )
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
            count += 1
        else:
            # Fallback for simpler pattern
            target_fallback = r'(href=["\']\{\%\s*url\s+[\'"]list_Attendance[\'"]\s*\%\}\s*["\']\s*>\s*<\s*span[^>]*>.*?Attended List</a>)'
            new_content = re.sub(
                target_fallback,
                r'\1\n<a class="nav-item" href="{% url \'list_payments\' %}"><span class="icon">💰</span>Payment List</a>',
                content,
                flags=re.IGNORECASE
            )
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Updated (fallback) {filename}')
                count += 1

print(f"Total files updated: {count}")
