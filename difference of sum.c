int differenceOfSum(int* nums, int size) {
    int ele_sum=0,dig_sum=0,rem,res=0;
    for(int i=0;i<size;i++)
    ele_sum+=nums[i];
    for(int i=0;i<size;i++){
        while(nums[i]!=0){
            rem=nums[i]%10;
            dig_sum+=rem;
            nums[i]/=10;
        }
    }
    res=ele_sum-dig_sum;
    if(res>=0)
    return res;
    return res*(-1);
}
