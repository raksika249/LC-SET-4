int thirdMax(int* nums,int numsSize) {
    int temp;
    for(int i=0;i<numsSize-1;i++){
        for(int j=i+1;j<numsSize;j++){
            if(nums[i]<nums[j])
            {
                temp=nums[i];
                nums[i]=nums[j];
                nums[j]=temp;
            }
        }
    }
    for(int i=0;i<numsSize-1;){
        if(nums[i]==nums[i+1]){
        for(int j=0;j<numsSize-1;j++){
        if(nums[j]==nums[j+1]){
            for(int k=j;k<numsSize-1;k++){
                nums[k]=nums[k+1];
            }
            numsSize--;
        }
    }
    }
    else
    i++;
    }   
    if(numsSize<3)
    return nums[0];
    return nums[2];
}
