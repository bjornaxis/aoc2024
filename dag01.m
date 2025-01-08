load input.txt
format long
sum(abs(sort(input(:,1))-sort(input(:,2))))

ss = 0;
for i = input(:,1)'
ss = ss + sum(input(:,2)==i)*i;
end
ss
