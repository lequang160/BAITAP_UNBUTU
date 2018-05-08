clear;
echo "chuong trinh dem so dong cua mot tap tin $1";
{
n=0;
while read line
do
n=$(($n + 1));
done
echo "So dong cua file $1 = $n";
}<$1
exit 0;
