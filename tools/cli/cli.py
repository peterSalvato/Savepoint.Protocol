
import argparse
from commands import extract, savepoint

def main():
    parser = argparse.ArgumentParser(prog='sp')
    subparsers = parser.add_subparsers(title='subcommands', dest='command')

    # Extract command
    extract_parser = subparsers.add_parser('extract')
    extract_parser.add_argument('--source', help='Path to conversations.json')
    extract_parser.add_argument('--output', help='Directory to write output files')
    extract_parser.add_argument('--prefix', help='Filter conversations by title prefix (e.g. AE, SP, etc.)')
    extract_parser.set_defaults(func=extract.run)

    # Savepoint extract command
    sp_extract_parser = subparsers.add_parser('savepoint-extract')
    sp_extract_parser.add_argument('--source', help='Path to conversations.json')
    sp_extract_parser.add_argument('--output', help='Directory to write savepoints to')
    sp_extract_parser.add_argument('--prefix', help='Only extract Savepoints from titles starting with this prefix')
    sp_extract_parser.add_argument('--suffix', help='Add this suffix to output filenames')
    sp_extract_parser.add_argument('--dates', help='Date range filter in format YYYY-MM-DD:YYYY-MM-DD')
    sp_extract_parser.set_defaults(func=savepoint.extract)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
