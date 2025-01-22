# -*- coding: utf-8 -*-
"""fastasorting.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J2nQU5Pq2DRRn-U_JNDHLyzhuenoUjCT
"""

import os
from Bio import SeqIO

# Especifica la carpeta donde están los archivos FASTA
fasta_folder = input("Insert Fasta folder route to scan: ")  # Cambia al nombre de tu carpeta

# Lista para almacenar las secuencias con su conteo de adeninas
sequences_with_a_count = []

# Leer todos los archivos en la carpeta
for file_name in os.listdir(fasta_folder):
    if file_name.endswith(".fasta"):  # Asegúrate de que sean archivos FASTA
        file_path = os.path.join(fasta_folder, file_name)
        for record in SeqIO.parse(file_path, "fasta"):
            a_count = record.seq.count("A")  # Cuenta adeninas
            sequences_with_a_count.append((record.id, a_count, str(record.seq), file_name))

# Ordenar las secuencias por la cantidad de adeninas en orden descendente
sequences_with_a_count.sort(key=lambda x: x[1], reverse=True)

# Mostrar las secuencias ordenadas
print("\nSequences sorted by adenine count:")
for seq_info in sequences_with_a_count:
    print(f"File: {seq_info[3]} | ID: {seq_info[0]}, Adenine Count: {seq_info[1]}")
    print(f"Sequence: {seq_info[2]}\n")