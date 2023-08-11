import argparse
from similarity import concat, top_generator
from similarity import embed
import similarity.sanitize as sanitizer
import similarity.cleanup as cleanup

def run(paths, content_identifier, top, highlights_identifier, out_dir = 'out'):
    sanitized_files = sanitizer.sanitize_files(paths, out_dir)
    cleaned_files = cleanup.clean(content_identifier, sanitized_files, out_dir, ['example'])
    concat_file = concat.concat(cleaned_files, out_dir)
    embedded = embed.embed(content_identifier, concat_file, out_dir)
    res = top_generator.get_top_similarities(embedded, top, highlights_identifier, out_dir)
    print(res)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate similarities between JSON objects (e.g. blog posts represented in JSON format.)")

    parser.add_argument("paths", nargs='+', help="List of file paths to process")
    parser.add_argument("--content_identifier", required=True, type=str, help="Identifier for the content in JSON files")
    parser.add_argument("--top", required=False, default = 5, type=int, help="How many top entries should be shown in final file")
    parser.add_argument("--top_identifier", required=True, type=str, help="Identifier for top similarities. Must be existing key of initial dataset.")
    parser.add_argument("--out", required=False, default="out", type=str, help="Output directory")

    args = parser.parse_args()
    
    run(args.paths, args.content_identifier, args.top, args.top_identifier, args.out)