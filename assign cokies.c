int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
int findContentChildren(int* g, int gSize, int* s, int sSize) {
    int i=0,j=0,content=0,temp;
    qsort(s,sSize,sizeof(int),compare);
    qsort(g,gSize,sizeof(int),compare);
    while(i<gSize&&j<sSize){
        if(g[i]<=s[j]){
            content++;
            i++;
            j++;
        }
        else
        j++;
    }
    return content;
}
