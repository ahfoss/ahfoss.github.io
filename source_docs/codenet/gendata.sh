# Download small subsample of codenet data.
wget https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Mini_Project_CodeNet.tar.gz

# Unpack tar file.
tar -zxvf Mini_Project_CodeNet.tar.gz

# Create one big file with all cpp
cat data/p*/C++/s*.cpp > cpp_raw.txt
cat data/p*/C/s*.c > c_raw.txt
cat data/p*/Go/s*.go > go_raw.txt
cat data/p*/Java/s*.java > java_raw.txt
cat data/p*/Python/s*.py > python_raw.txt
cat data/p*/Ruby/s*.rb > ruby_raw.txt

# Remove files we don't need anymore.
rm Mini_Project_CodeNet.tar.gz
rm -vrf metadata/
rm -vrf data/
