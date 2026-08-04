class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> arr = {0};

        for(int i = 1; i <= n; i++){
            int res = 0;
            int curr = i;
            while(curr > 0){
                if(curr % 2 == 1){
                    res++;
                }
                curr = curr >> 1;
            }
            arr.push_back(res);
        }
        return arr;
    }
};
