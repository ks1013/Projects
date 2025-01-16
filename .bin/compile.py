#!/usr/bin/env python3

import argparse
import os
import pathlib
import subprocess
import sys

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

def eprint(*args, **kwargs):
    print("\033[0;31m", file=sys.stderr, end='')
    print(*args, file=sys.stderr, **kwargs)
    print("\033[0m", file=sys.stderr, end='')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', nargs='?')
    args = parser.parse_args()

    if args.directory:
        project_dir = BASE_DIR / args.directory
        if not project_dir.exists():
            eprint(f"Project '{args.directory}' does not exist")
            return 1
    else:
        cwd = pathlib.Path(os.getcwd()).resolve()
        if cwd.parent != BASE_DIR:
            eprint("Please run the 'compile' command in a project directory, or specify a project name")
            return 1
        project_dir = cwd

    build_dir = project_dir / 'meson-build'
    if not build_dir.exists():
        os.environ['CC'] = 'clang'
        p = subprocess.run(
            ['meson', 'setup', '--buildtype', 'debug', build_dir],
            cwd=project_dir
        )
        if p.returncode != 0:
            subprocess.run(['rm', '-rf', build_dir], cwd=project_dir)
            return p.returncode

    subprocess.run(['meson', 'compile'], cwd=build_dir)

    return 0

if __name__ == "__main__":
    sys.exit(main())
