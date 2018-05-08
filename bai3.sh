
clear;

echo "Nhap ten thu muc ";
read dir_name;
mkdir $dir_name;
if test $? -eq 0; then
clear;
echo "thu muc $dir_name da dc tao";
else
clear;
echo "Khong the tao thu muc ten $dir_name"
fi
