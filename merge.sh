#!/bin/bash

# Nome dos arquivos a serem mesclados
file1="main.py"
file2="src/main.py"
# Nome do arquivo de saída
output_file="main.py"
# Mesclar os arquivos
cat "$file1" "$file2" > "$output_file"