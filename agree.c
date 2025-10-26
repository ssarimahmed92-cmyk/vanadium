int main(void)
{
   char c = get_char("do you agree? ");

   if (c == 'y' || c == 'Y')
   {
    printf("agreed.\n");
   }
   if (c == 'n' || c == 'N')
   {
    printf("not agreed.\n");
   }
}
