clear;
echo "Chuong trinh dem so tu cua mot file $1";
{
n=0;
while read line
do
	for wd in $line
	do
		n=$(($n + 1))
	done
done
}<$1
echo "so tu cua file $1 la : $n"
exit 0;

