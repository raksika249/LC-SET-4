int countKeyChanges(char* s) {
    int i=0,change=0;
    while(s[i+1]!='\0'){
        if(s[i]!=s[i+1]&&s[i]!=s[i+1]+32&&s[i]!=s[i+1]-32){
            change++;
            printf("%d ",i);
        }
        i++;
    }
    return change;
}
