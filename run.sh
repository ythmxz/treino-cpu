#!/usr/bin/env bash

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
    echo "Uso: ./run.sh <script> <prefixo_entrada> <prefixo_saida>"
    exit 1
fi

script="$1"
prefixo_entrada="$2"
prefixo_saida="$3"

for arquivo in $(ls ${prefixo_entrada}* | sort -V); do
    echo Rodando $arquivo
    if ! python3 "$script" < "${arquivo}" | diff - "${prefixo_saida}${arquivo#"$prefixo_entrada"}" --strip-trailing-cr; then
        break
    fi
done
