if [[ -z "$1" || -z "$2" || -z "$3" ]]; then
    echo "Uso: ./run.sh <script> <prefixo_entrada> <prefixo_saida>"
    exit 1
fi

script="$1"
prefixo_entrada="$2"
prefixo_saida="$3"

for arquivo in ${prefixo_entrada}*; do
    echo Rodando $arquivo
    python "$script" < "${arquivo}" | diff - "${prefixo_saida}${arquivo/#$prefixo_entrada}" --strip-trailing-cr
done
