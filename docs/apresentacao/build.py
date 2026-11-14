"""Build the standalone presentation from its fragment, including on Windows."""
from pathlib import Path
import sys


def build(output: Path | None = None) -> Path:
    folder = Path(__file__).resolve().parent
    output = output or folder.parent / "index.html"
    fragment = (folder / "apresentacao-fragmento-artefato.html").read_text(encoding="utf-8")
    boundary = fragment.index("</style>") + len("</style>")
    document = (
        '<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + fragment[:boundary] + "\n</head>\n<body>" + fragment[boundary:]
        + "\n</body>\n</html>\n"
    )
    output.write_text(document, encoding="utf-8", newline="\n")
    return output


if __name__ == "__main__":
    print(f"built {build(Path(sys.argv[1]) if len(sys.argv) > 1 else None)}")
