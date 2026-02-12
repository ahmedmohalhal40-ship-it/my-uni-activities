import os

folder_path = r'D:\New folder'

# خريطة الأسامي الجديدة {الاسم القديم : الاسم الجديد}
rename_map = {
    'project.html': 'index.html',
    'add.html': 'admin-add-activity.html'
}

def finalize_for_github():
    # 1. تعديل الروابط جوه محتوى الملفات الأول قبل ما نغير أساميها
    for filename in os.listdir(folder_path):
        if filename.endswith('.html'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # استبدال كل اسم قديم بالجديد جوه الكود
            for old_name, new_name in rename_map.items():
                content = content.replace(f"'{old_name}'", f"'{new_name}'")
                content = content.replace(f'"{old_name}"', f'"{new_name}"')
                content = content.replace(f'href="{old_name}"', f'href="{new_name}"')

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
    
    # 2. تغيير أسامي الملفات فعلياً في الفولدر
    for old_name, new_name in rename_map.items():
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        
        if os.path.exists(old_path):
            if os.path.exists(new_path):
                os.remove(new_path) # مسح النسخة القديمة لو موجودة
            os.rename(old_path, new_path)
            print(f"✅ تم تغيير اسم {old_name} إلى {new_name}")

if __name__ == "__main__":
    finalize_for_github()
    print("\n🚀 كدة ملفاتك جاهزة تترفع على GitHub واللينكات متظبطة!")