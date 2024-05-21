import os
import pypandoc

input_dir = "Interactions_Client-Serveur/chapters"
output_dir = "pdf"
output_filename = "Interactions_Client-Serveur.pdf"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Build the pandoc options as a string
pandoc_cmd = [
    "--include-in-header", "pandoc/chapter_break.tex",
    "-V", "linkcolor:blue",
    "-V", "geometry:a4paper",
    "-V", "geometry:margin=1.8cm",
    "-V", "mainfont=DejaVu Serif",
    "-F", "mermaid-filter",
    "--pdf-engine=xelatex",
]

output_path = os.path.join(output_dir, output_filename)
# Convert all markdown files in the chapters/ subdirectory.
pypandoc.convert_file(
    os.path.join(input_dir, "01-introduction.md"), to="pdf", format="markdown",
    outputfile=output_path,
    extra_args=pandoc_cmd,
)

print(f"Conversion completed. Output saved to: {output_path}")