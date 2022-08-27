#!/bin/sh
# compile
pyinstaller --clean --onefile "TermDrop_Encoder.py"
mv dist/* .
rm -rf build
rm -rf dist
rm TermDrop_Encoder.spec
echo "Compilation Completed"