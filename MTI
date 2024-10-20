#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
// اتحاد
void printUnion(const vector<int>& amor1, const vector<int>& amor2,
    const string& name1, const string& name2)
{
    set<int> unionSet(amor1.begin(), amor1.end());
    unionSet.insert(amor2.begin(), amor2.end()); // set cannot repet item
    cout << "Union of " << name1 << " and " << name2 << ": ";
    for (int num : unionSet) {
        cout << num << " ";
    }
    cout << endl;
}

// التقاطع
void printIntersection(const vector<int>& amor1, const vector<int>& amor2, const string& name1, const string& name2) {
    vector<int> intersectionSet;
    for (int num : amor1)
        if (find(amor2.begin(), amor2.end(), num) != amor2.end())
            intersectionSet.push_back(num);

    cout << "Intersection of " << name1 << " and " << name2 << ": ";
    for (int num : intersectionSet) {
        cout << num << " ";
    }
    cout << endl;
}

//  (A - B)
void printDifference(const vector<int>& amor1, const vector<int>& amor2, const string& name1, const string& name2) {
    vector<int> differenceSet;
    for (int num : amor1)
        if (find(amor2.begin(), amor2.end(), num) == amor2.end())
            differenceSet.push_back(num);

    cout << "Difference of " << name1 << " and " << name2 << ": ";
    for (int num : differenceSet) {
        cout << num << " ";
    }
    cout << endl;
}

// المكمله
void printComplement(const vector<int>& amor1, const vector<int>& universalSet, const string& name) {
    vector<int> complementSet;
    for (int num : universalSet)
        if (find(amor1.begin(), amor1.end(), num) == amor1.end())
            complementSet.push_back(num);

    cout << "Complement of " << name << ": ";
    for (int num : complementSet) {
        cout << num << " ";
    }
    cout << endl;
}

// الجزء
void checkSubset(const vector<int>& subset, const vector<int>& amor2, const string& subsetName, const string& supersetName) {
    bool isSubset = false;
    for (int num : subset)
        if (find(amor2.begin(), amor2.end(), num) == amor2.end()) {
            isSubset = true;
            break;
        }

    cout << "Is " << subsetName << " a subset of " << supersetName << "? " << (isSubset ? "Yes" : "No") << endl;
}

int main() {
    vector<int> universalSet = {1, 2, 3, 4, 5, 6, 7, 8};
    vector<int> A = {2, 4, 8, 6, 6};
    vector<int> B = {3, 4, 5, 6};
    vector<int> C = {7, 8};
    vector<int> D = {1, 3, 5, 7};
    // test
    printUnion(A, B, "A", "B");
    printIntersection(C, D, "C", "D");
    printDifference(A, B, "A", "B");
    printComplement(A, universalSet, "A");
    checkSubset(A, B, "A", "A");

    return 0;
}
