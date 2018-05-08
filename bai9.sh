clear;
echo "Chuong trinh tim dong co do dai lon nhat trong mot tap tin $1";
{

max=0;
i=0;
res=0;
while read line
do
	
	n=0;
	for wd in $line
	do
		n=$(($n + 1))
	done
	if [ $n -gt $max ]; 
	then
		max=$n;
		res=$i;	
	else
		max=$max;
	fi
	i=$(($i + 1))
done
echo "Dong co do dai lon nhat cua $1 la dong so : $res"
}<$1
exit 0
