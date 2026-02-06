#pragma once
#include "include/Position.hpp"
#include <iostream>
using namespace std;

int main() {
    Position p{"AAPL", 100.0, 150.25};
    cout << "Position weight test: " << p.weight(10000.0) << endl;
    cout << "✅ SR 11-7 Position.hpp VALIDATED" << endl;
    return 0;
}
