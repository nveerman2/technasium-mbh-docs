from pathlib import Path
from datetime import datetime
import re

# ============================================================
# Repo configuratie (relatief, werkt lokaal + in GitHub Actions)
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parents[1]
DOCS_DIR = PROJECT_DIR / "docs"
YML_FILE = PROJECT_DIR / "mkdocs.yml"
LOG_FILE = PROJECT_DIR / "logs" / "update_nav.log"

SITE_URL = "https://technasiummbh.nl/"
REPO_URL = "https://github.com/nveerman2/technasium-mbh-docs"

SKIP_FOLDERS = {"img", "overrides", ".git", "__pycache__"}
FORCE_REGEN_INDEX = True  # alle map index.md opnieuw genereren behalve homepage

# Zorg dat logmap bestaat
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

# ============================================================
# Logging
# ============================================================

def log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    line = f"{timestamp} {message}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# ============================================================
# Helpers voor sortering & titels
# ============================================================

def split_order(name: str):
    """Haal leading nummer weg en geef (nummer, rest)."""
    m = re.match(r"^(\d+)[-_ ]?(.*)$", name)
    if m:
        return int(m.group(1)), (m.group(2) or "")
    return None, name


def order_key(p: Path):
    """Eerst nummer, dan alfabetisch."""
    n, rest = split_order(p.stem if p.is_file() else p.name)
    return (999999 if n is None else n, rest.lower())


def pretty_name(name: str):
    """Verwijder nummerprefix voor weergave."""
    _, rest = split_order(name)
    return rest or name


def safe_title(text: str):
    return pretty_name(text).replace("-", " ").replace("_", " ").title()


# ============================================================
# Automatische indexpagina per map (behalve homepage)
# ============================================================

def update_section_index(folder_path: Path):
    index_file = folder_path / "index.md"

    # Homepage met rust laten
    if folder_path == DOCS_DIR:
        log("Skip homepage index.md")
        return

    if index_file.exists():
        log(f"Overschrijf index.md in {folder_path}")
    else:
        log(f"Genereer nieuwe index.md in {folder_path}")

    lines = [
        f"# {safe_title(folder_path.name)}",
        "",
        "Overzicht:",
        ""
    ]

    entries = []

    # Eerst submappen
    for sub in sorted(folder_path.iterdir(), key=order_key):
        if sub.is_dir() and not sub.name.startswith("."):
            sub_index = sub / "index.md"
            if sub_index.exists():
                name = safe_title(sub.name)
                rel = sub.relative_to(folder_path).as_posix() + "/index.md"
                entries.append(f"- [{name}]({rel})")

    # Dan markdown bestanden
    for file in sorted(folder_path.glob("*.md"), key=order_key):
        if file.name != "index.md":
            name = safe_title(file.stem)
            rel = file.relative_to(folder_path).as_posix()
            entries.append(f"- [{name}]({rel})")

    lines.extend(entries)
    index_file.write_text("\n".join(lines), encoding="utf-8")


# ============================================================
# Navigatie-items verzamelen (2 niveaus diep)
# ============================================================

def collect_nav_items(folder_path: Path):
    items = []

    if folder_path != DOCS_DIR:
        update_section_index(folder_path)

    # Submappen = niveau 1
    for subfolder in sorted(folder_path.iterdir(), key=order_key):
        if (
            subfolder.is_dir()
            and subfolder.name not in SKIP_FOLDERS
            and not subfolder.name.startswith(".")
        ):
            subitems = []

            # Niveau 2: markdown in submap
            for md in sorted(subfolder.glob("*.md"), key=order_key):
                if md.name != "index.md":
                    subitems.append({
                        safe_title(md.stem): md.relative_to(DOCS_DIR).as_posix()
                    })

            # Voeg altijd index bovenaan toe als die bestaat
            index_file = subfolder / "index.md"
            if index_file.exists():
                subitems.insert(0, {
                    safe_title(subfolder.name): index_file.relative_to(DOCS_DIR).as_posix()
                })

            if subitems:
                items.append({safe_title(subfolder.name): subitems})

    # Markdown bestanden in root docs/
    for md_file in sorted(folder_path.glob("*.md"), key=order_key):
        if md_file.name != "index.md":
            items.append({
                safe_title(md_file.stem): md_file.relative_to(DOCS_DIR).as_posix()
            })

    # Homepage altijd bovenaan
    index_file = DOCS_DIR / "index.md"
    if index_file.exists():
        items.insert(0, {"Home": "index.md"})

    return items


# ============================================================
# mkdocs.yml schrijven
# ============================================================

def write_yml():
    log("Start genereren van mkdocs.yml")

    lines = [
        "site_name: Technasium MBH",
        f"site_url: {SITE_URL}",
        "",
        "theme:",
        "  name: material",
        "  features:",
        "    - content.tabs.link",
        "    - content.tooltips",
        "    - content.code.copy",
        "  logo: img/logo.png",
        "  favicon: img/favicon.ico",
        "  language: nl",
        "  custom_dir: overrides",
        "  palette:",
        "    primary: indigo",
        "    accent: purple",
        "  font:",
        "    text: Roboto",
        "    code: Roboto Mono",
        "",
        "extra_css:",
        "  - https://fonts.googleapis.com/icon?family=Material+Icons",
        "  - extra.css",
        "",
        "markdown_extensions:",
        "  - admonition",
        "  - pymdownx.tabbed",
        "  - pymdownx.details",
        "  - pymdownx.tasklist",
        "  - pymdownx.highlight",
        "  - pymdownx.superfences",
        "  - pymdownx.emoji",
        "",
        "nav:"
    ]

    nav_items = collect_nav_items(DOCS_DIR)

    for item in nav_items:
        for title, path in item.items():
            if isinstance(path, list):
                lines.append(f"  - {title}:")
                for subitem in path:
                    for sub_title, sub_path in subitem.items():
                        lines.append(f"    - {sub_title}: {sub_path}")
            else:
                lines.append(f"  - {title}: {path}")

    lines.extend([
        "",
        f"repo_url: {REPO_URL}",
        "repo_name: GitHub"
    ])

    YML_FILE.write_text("\n".join(lines), encoding="utf-8")
    log("mkdocs.yml opgeslagen")


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    log("=== Update MkDocs navigatie gestart ===")
    write_yml()
    log("=== Klaar ===")
