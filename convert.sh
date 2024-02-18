#!/bin/bash

# Diretório de origem dos arquivos .ui
ui_dir=screens

# Verifica se o diretório de origem existe
if [ ! -d "$ui_dir" ]; then
    echo "Diretório $ui_dir não encontrado."
    exit 1
fi


# Varre todos os arquivos .ui no diretório de origem
for ui_file in "$ui_dir"/*.ui; do
    # Extrai o nome do arquivo sem a extensão
    base_name=$(basename "$ui_file" .ui)
    
    # Caminho completo para o arquivo de saída .py
    py_file="./$base_name.py"
    
    # Converte o arquivo .ui em .py
    pyuic5 -o "$py_file" "$ui_file"
    
    echo "Arquivo $ui_file convertido para $py_file"
done

echo "Conversão concluída."