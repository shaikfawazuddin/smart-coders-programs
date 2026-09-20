cp, sp = map(float, input().split())
if sp > cp: print('Profit:', sp - cp)
elif cp > sp: print('Loss:', cp - sp)
else: print('No profit, no loss')
