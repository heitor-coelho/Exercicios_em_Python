A, B, C = map(int, input().split())
X, Y  = map(int, input().split())
if A<=X and B<=Y:
   print('S')
elif A<= X and C<=Y:
   print('S')
elif B<= X and A<=Y:
   print('S')
elif B<= X and C<=Y:
   print('S')
elif C<= X and A<=Y:
   print('S')
elif C<=X and B<=Y:
   print('S')
else:
   print('N')