import os
import subprocess
import zipfile
import shutil

base_dir = r"c:\Users\ADMIN\Downloads\Collexa"
zip_path = r"c:\Users\ADMIN\Downloads\Collexa_Enterprise_ERP.zip"

def run(cmd):
    p = subprocess.run(cmd, shell=True, cwd=base_dir, capture_output=True, text=True)
    return p.stdout

run("git add .")
run('git commit -m "chore(build): remove BOM from package.json and verify clean production build"')

# Create final zip
exclude_dirs = {"myenv", "node_modules", "__pycache__", "dist", "build", ".venv", ".next", ".vscode", ".idea", ".pytest_cache"}
exclude_extensions = {".pyc", ".pyd", ".zip"}

file_count = 0
git_file_count = 0
total_bytes = 0

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in exclude_extensions:
                continue
            if file == "Collexa_Enterprise_ERP.zip":
                continue
            if ".env" in file.lower():
                continue
                
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, source_dir := base_dir)
            zipf.write(full_path, os.path.join("Collexa", rel_path))
            file_count += 1
            if ".git" in rel_path.split(os.sep):
                git_file_count += 1
            total_bytes += os.path.getsize(full_path)

print(f"ZIP package finalized: {file_count} files ({git_file_count} git files), {os.path.getsize(zip_path)/(1024*1024):.2f} MB")
shutil.copyfile(zip_path, os.path.join(base_dir, "Collexa_Enterprise_ERP.zip"))
