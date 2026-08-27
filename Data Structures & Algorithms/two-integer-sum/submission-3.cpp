class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        int i = 0;
        vector<int> ans;
        while(i < n){
            for (int j = 0; j < n; j++){
                
               
                if(nums[i] + nums[j] == target){
                    if(i == j){
                    continue;
                }
                    ans.push_back(i);
                    ans.push_back(j);
                    return ans;
                }

            }
            i++;
        }
        
    }
};
