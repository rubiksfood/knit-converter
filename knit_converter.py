#! /usr/bin/env python3
import argparse
from pathlib import Path

from file_conversion import pdf_to_docx, docx_to_pdf
from term_conversion import convert_terms_in_docx
from terminology import US_GB_DICT

# Parse command-line arguments
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert US knitting terminology to UK equivalents in PDF knitting patterns."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        required=True,
        help="Input directory containing PDF files.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        required=True,
        help="Output directory where converted PDFs will be written.",
    )
    parser.add_argument(
        "--prefix",
        default="gb_",
        help="Prefix for output PDF filenames (default: gb_).",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip conversion if the output PDF already exists.",
    )
    parser.add_argument(
        "--keep-docx",
        action="store_true",
        help="Keep intermediate .docx files (useful for debugging).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_dir: Path = args.input
    output_dir: Path = args.output
    prefix: str = args.prefix

    # Check input directory exists
    if not input_dir.exists() or not input_dir.is_dir():
        print(f"ERROR: Input directory does not exist or is not a directory: {input_dir}")
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)

    # Find all PDF files in the input directory
    pdf_files = sorted(p for p in input_dir.iterdir() if p.is_file() and p.suffix.lower() == ".pdf")
    if not pdf_files:
        print(f"No PDF files found in: {input_dir}")
        return 0

    # Keep track of stats for reporting
    converted = 0
    skipped = 0
    failed = 0

    for pdf_path in pdf_files:
        docx_temp = output_dir / f"{pdf_path.stem}.docx"
        output_pdf = output_dir / f"{prefix}{pdf_path.name}"

        # Skip if output PDF already exists
        if args.skip_existing and output_pdf.exists():
            print(f"Skipping (already exists): {output_pdf.name}")
            skipped += 1
            continue

        try:
            pdf_to_docx(str(pdf_path), str(docx_temp))
            convert_terms_in_docx(str(docx_temp), US_GB_DICT)
            docx_to_pdf(str(docx_temp), str(output_pdf))
            print(f"Converted: {pdf_path.name} -> {output_pdf.name}")
            converted += 1
        except Exception as e:
            print(f"FAILED: {pdf_path.name} ({e})")
            failed += 1
        finally:
            if not args.keep_docx:
                try:
                    docx_temp.unlink(missing_ok=True)  # For python 3.8+
                except TypeError:
                    if docx_temp.exists():
                        docx_temp.unlink()

    # Report summary
    print(f"\nDone. Converted: {converted}, Skipped: {skipped}, Failed: {failed}")
    print(f"Output directory: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())