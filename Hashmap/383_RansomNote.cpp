class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int idx = -1;
        for(auto c: ransomNote) {
            cout << c << endl;
            if( (idx = magazine.find(c)) != -1) {
               magazine[idx] = ' ';
            }else{
                return false;
            }
        }
        return true;
    }
};