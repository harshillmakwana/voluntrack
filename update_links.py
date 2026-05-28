import os
import re
directory = r'd:\Project\volunteer_project\volunteer_pro\templates\userapp'
count = 0
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = re.sub(r'\{%\s*url\s+[\'"]org_livechat[\'"]\s*%\}', "{% url 'chat_index' %}", content)
        new_content = re.sub(r'\{%\s*url\s+[\'"]vol_livechat[\'"]\s*%\}', "{% url 'chat_index' %}", new_content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
            count += 1
print(f"Total updated: {count}")
