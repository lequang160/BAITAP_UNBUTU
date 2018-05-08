clear;
echo "giai thua cua $1 la :";
index=1;
gt=1;
while [ $index -le $1 ]
do
	gt=$(($gt * $index))
	index=$(($index + 1))
done
echo "Giai thua cua $1 la : $gt";
exit 0
