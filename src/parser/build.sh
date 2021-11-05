# Build Python version
antlr4 -Dlanguage=Python3 -o python Command.g4
# Build Java version
antlr4 -o java Command.g4
javac java/Command*.java
# Test with Java
(cd java; grun Command command -tokens ../input.txt)