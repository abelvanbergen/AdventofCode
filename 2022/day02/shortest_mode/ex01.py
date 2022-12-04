#evolution shortest mode
p=[[4,8,3],[1,5,9],[7,2,6]]
print(sum([p[ord(i)-65][ord(k)-88]for i,j,k in open("i").read().splitlines()]))

print(sum([[[4,8,3],[1,5,9],[7,2,6]][ord(i)-65][ord(k)-88]for i,j,k in open("i").read().splitlines()]))

print(sum([int("483159726"[3*(ord(i)-65)+ord(k)-88])for i,j,k in open("i").read().splitlines()]))
print(sum(int("483159726"[3*(ord(i)-65)+ord(k)-88])for i,j,k,l in open("i")))
print(sum(int("915672348"[ord(l[0])%3*3+ord(l[2])%3])for l in open("i")))
print(sum(57-b"084327651"[x[0]%3*3+x[2]%3]for x in open("i","rb")))