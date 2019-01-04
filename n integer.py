Unsigned long long firstkdigits(int n,int k) 
{ 
 Unsigned long long product = 3; 
  for (int i=0; i<n; i++) 
      product *= n; 
   while ((int)(product / pow(10,k)) != 0) 
      product = product / 10; 
   return product; 
} 
int main() 
{ 
   int n=15; 
   int k=4; 
   cout << firstkdigits(n,k); 
   return 0; 
} 
