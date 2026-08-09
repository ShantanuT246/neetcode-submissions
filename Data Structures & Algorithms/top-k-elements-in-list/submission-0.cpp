class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> mpp;
        for (int num : nums) {
            mpp[num]++;
        }

        vector<vector<int>> arr(nums.size() + 1);

        for (auto it : mpp) {
            arr[it.second].push_back(it.first);
        }

        vector<int> ans;

        for (int i = arr.size() - 1; i >= 0 && ans.size() < k; i--) {
            for (int num : arr[i]) {
                ans.push_back(num);

                if (ans.size() == k) {
                    break;
                }
            }
        }

        return ans;
    }
};