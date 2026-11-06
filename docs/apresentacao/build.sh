#!/usr/bin/env bash
# Builds the standalone HTML (with document skeleton) from the artifact fragment.
set -e
SRC="$(dirname "$0")/apresentacao-fragmento-artefato.html"
OUT="${1:-$(dirname "$0")/../index.html}"
{ printf '<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'; cat "$SRC"; printf '\n</body>\n</html>\n'; } > "$OUT"
python3 - "$OUT" <<'PY'
import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read(); i=s.index('</style>')+len('</style>'); s=s[:i]+'\n</head>\n<body>'+s[i:]; open(p,'w',encoding='utf-8').write(s)
PY
echo "built $OUT"
