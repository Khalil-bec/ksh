#!/usr/bin/env bash
set -e

echo -e "\n Désinstallation de ksh..."
LAUNCHER="/usr/local/bin/ksh"
if [ -f "$LAUNCHER" ]; then
    sudo rm "$LAUNCHER"
    echo "Lanceur supprimé."
else
    echo "Lanceur non trouvé, rien à supprimer."
fi

echo -e "✓ Désinstallation terminée."
echo -e "Tes alias dans ~/.ksh_aliases sont conservés.\n"
