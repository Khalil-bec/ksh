#!/usr/bin/env bash
set -e

INSTALL_DIR="$(cd "$(dirname "$0")" && pwd)"
LAUNCHER="/usr/local/bin/ksh"
REQ_FILE="$INSTALL_DIR/requirements.txt"

echo "Installation de ksh..."

# Python 3 installé ?
if ! command -v python3 &>/dev/null; then
    echo "Erreur : Python 3 introuvable"
    exit 1
fi

#installation des dépendances
if [ -f "$REQ_FILE" ]; then
    pip3 install --user -r "$REQ_FILE" --break-system-packages --quiet 2>/dev/null || \
    pip3 install --user -r "$REQ_FILE" --quiet
else
    echo "Fichier requirements.txt introuvable, impossible d'installer les dépendances."
    exit 1
fi

# Fichier alias
[ ! -f "$HOME/.ksh_aliases" ] && echo "{}" > "$HOME/.ksh_aliases"

# Lanceur global
echo "#!/usr/bin/env bash
exec python3 \"$INSTALL_DIR/main.py\" \"\$@\"" | sudo tee "$LAUNCHER" > /dev/null
sudo chmod +x "$LAUNCHER"

echo "Fait. Lance le shell avec : ksh"