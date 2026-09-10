from pathlib import Path
import sys

if len(sys.argv) != 3:
    raise SystemExit("Usage: python scripts/new_project_routes.py PROJECT_ID PROJECT_SLUG")

project_id, slug = sys.argv[1], sys.argv[2]
root = Path(__file__).resolve().parents[1]
folder = root / "_projects"
folder.mkdir(exist_ok=True)

files = {
    folder / f"{slug}-en.md": f"""---\nlang: en\nproject_id: {project_id}\npermalink: /projects/{slug}/\nalternate_url: /zh/projects/{slug}/\n---\n""",
    folder / f"{slug}-zh.md": f"""---\nlang: zh\nproject_id: {project_id}\npermalink: /zh/projects/{slug}/\nalternate_url: /projects/{slug}/\n---\n""",
}
for path, content in files.items():
    if path.exists():
        print(f"Skip existing: {path.relative_to(root)}")
    else:
        path.write_text(content, encoding="utf-8")
        print(f"Created: {path.relative_to(root)}")
