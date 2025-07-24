#!/usr/bin/env python3
"""
Script to convert PDF files to JSON using pdf_parsing, then convert JSON to Markdown format.
"""

import json
import os
from pathlib import Path
from src.pdf_parsing import PDFParser, JsonReportProcessor


def convert_pdf_to_json(pdf_path, output_dir):
    """
    Convert a PDF file to JSON format using the PDFParser.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_dir (str): Directory to save the JSON output
        
    Returns:
        str: Path to the generated JSON file
    """
    # Create PDF parser
    parser = PDFParser(output_dir=Path(output_dir))
    
    # Convert the PDF
    pdf_paths = [Path(pdf_path)]
    parser.parse_and_export(pdf_paths)
    
    # Return the path to the JSON file
    json_filename = Path(pdf_path).stem + ".json"
    json_path = Path(output_dir) / json_filename
    return str(json_path)


def convert_json_to_markdown(json_path, output_path):
    """
    Convert JSON file to Markdown format.
    
    Args:
        json_path (str): Path to the JSON file
        output_path (str): Path to save the Markdown output
    """
    # Read the JSON file
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract metadata
    metainfo = data.get('metainfo', {})
    content_pages = data.get('content', [])
    tables = data.get('tables', [])
    
    # Create a dictionary of tables for easy lookup
    table_dict = {table.get('table_id'): table for table in tables}
    
    # Create Markdown content
    markdown_content = []
    
    # Add metadata section
    markdown_content.append("# Document Metadata\n")
    for key, value in metainfo.items():
        markdown_content.append(f"- **{key}**: {value}")
    markdown_content.append("\n")
    
    # Add content sections
    markdown_content.append("# Document Content\n")
    
    for page in content_pages:
        # page_num = page.get('page', 0)
        # markdown_content.append(f"## Page {page_num}\n")
        
        content_items = page.get('content', [])
        for item in content_items:
            item_type = item.get('type', 'text')
            
            if item_type == 'table':
                # Handle table references - insert table content directly
                table_id = item.get('table_id')
                if table_id in table_dict:
                    table = table_dict[table_id]
                    # Insert table content directly in place
                    markdown_content.append(table.get('markdown', ''))
                    markdown_content.append("")
            elif item_type == 'picture':
                # Handle picture references
                picture_id = item.get('picture_id')
                markdown_content.append(f"[Picture {picture_id}]\n")
            elif item_type == 'section_header':
                # Handle section headers
                text = item.get('text', '')
                if text.strip():
                    # Convert to Markdown header (## for section headers)
                    markdown_content.append(f"### {text}")
                    markdown_content.append("")
            elif item_type == 'page_header':
                continue
            elif item_type == 'page_footer':
                continue
            elif item_type == 'list_item':
                # Handle list items
                text = item.get('text', '')
                if text.strip():
                    # Convert to Markdown list item
                    # Remove leading bullet point if present
                    cleaned_text = text.strip()
                    if cleaned_text.startswith(('·', '-', '*', '•')):
                        cleaned_text = cleaned_text[1:].strip()
                    markdown_content.append(f"- {cleaned_text}")
                    markdown_content.append("")
            else:
                # Handle other text content (including regular text)
                text = item.get('text', '')
                if text.strip():
                    markdown_content.append(text)
                    markdown_content.append("")
        
        markdown_content.append("")
    
    # Write to Markdown file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_content))


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert PDF to JSON then to Markdown')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('-o', '--output', help='Output directory for JSON and Markdown files')
    
    args = parser.parse_args()
    
    # Set default output directory if not provided
    if args.output:
        output_dir = args.output
    else:
        output_dir = "./output"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert PDF to JSON
    # print(f"Converting {args.pdf_path} to JSON...")
    # json_path = convert_pdf_to_json(args.pdf_path, output_dir)
    # print(f"JSON file created: {json_path}")
    json_path = "D:\project\RAG-Challenge-2\output\9d7a72445aba6860402c3acce75af02dc045f74d.json"
    # Convert JSON to Markdown
    markdown_path = os.path.join(output_dir, Path(args.pdf_path).stem + ".md")
    print(f"Converting {json_path} to Markdown...")
    convert_json_to_markdown(json_path, markdown_path)
    print(f"Markdown file created: {markdown_path}")


if __name__ == "__main__":
    main()