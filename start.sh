# !sh
mkdir $1
echo "
#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    freopen(\"input.txt\", \"r\", stdin);
    return 0;
}
" > $1/$1.cpp
> $1/input.txt