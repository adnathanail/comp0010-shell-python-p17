antlr4 -Dlanguage=Python3 -o python Command.g4
antlr4 -o java Command.g4
javac java/Command*.java

(cd java; grun Command command -tokens ../input.txt)