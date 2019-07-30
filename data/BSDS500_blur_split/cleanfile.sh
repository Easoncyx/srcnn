echo "Bash version ${BASH_VERSION}..."
for i in {1..400};
do
    eval "rm ./img/img"$i"_00.yuv"
    eval "rm ./img/img"$i"_00.yuv"
    eval "rm ./img/re_img"$i"_00.yuv"
done

mkdir ./img/input
mkdir ./img/label_hor
mkdir ./img/label_ver
mkdir ./img/label_dia
for i in {1..400};
do
    eval "mv ./img/img"$i"_00_recon.bmp ./img/input/"
    eval "mv ./img/img"$i"_01.bmp ./img/label_hor/"
    eval "mv ./img/img"$i"_02.bmp ./img/label_ver/"
    eval "mv ./img/img"$i"_03.bmp ./img/label_dia/"
done
