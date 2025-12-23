import argparse
import indexer
import searcher

def search(args) :
    searcher.search(
        args.name,
        args.ext,
        args.min_size,
        args.max_size,
        args.sort
    )



def index(args) :
    indexer.index(args.path)

def main() :
    # Main parser
    parser = argparse.ArgumentParser(description="File Name")
    # Subparsers
    subparsers = parser.add_subparsers(dest="command", help="Available Commands")
    search_parser = subparsers.add_parser("search", help="Searching")
    index_parser = subparsers.add_parser("index", help="Indexing")
    # Arguments inside each subparser
    search_parser.add_argument("--name", required=True, help="Search by filename")
    search_parser.add_argument("--ext", help="Filter by extension (e.g. .pdf)")
    search_parser.add_argument("--min-size", type=int, help="Minimum file size in bytes")
    search_parser.add_argument("--max-size", type=int, help="Maximum file size in bytes")
    search_parser.add_argument(
        "--sort",
        choices=["name", "size", "date"],
        default="name",
        help="Sort results by name, size, or date"
    )


    index_parser.add_argument("--path", type=str, help="Index with file path")
    # Parse args
    args = parser.parse_args()
    # Check which command was used
    if args.command == "search":
        search(args)
    elif args.command == "index":
        index(args)
    else:
        print("Search requires file name argument and Index requires file path as argument")

if __name__ == "__main__":
    main()