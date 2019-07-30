echo "Bash version ${BASH_VERSION}..."
for i in {1..400};
do
    eval "ffmpeg -i ./img/img"$i"_00.bmp -pix_fmt yuv420p ./img/img"$i"_00.yuv" #bmp to yuv
    eval "width=$(ffprobe -v error -show_entries stream=width -of csv=p=0:s=x ./img/img"$i"_00.bmp)" #get width
    eval "height=$(ffprobe -v error -show_entries stream=height -of csv=p=0:s=x ./img/img"$i"_00.bmp)" # get height
    eval "./TAppEncoderStatic -c encoder_intra_main.cfg --ReconFile=./img/img"$i"_00_recon.yuv --InputFile=./img/img"$i"_00.yuv --SourceWidth="$width" --SourceHeight="$height # encode
    eval "ffmpeg -s "$width"x"$height" -pix_fmt yuv420p -i ./img/img"$i"_00_recon.yuv ./img/img"$i"_00_recon.bmp" # yuv to bmp
done

# ffmpeg -i ./img/img1_00.bmp -pix_fmt yuv420p ./img/img1_00.yuv

# ./TAppEncoderStatic -c encoder_intra_main.cfg --ReconFile=re_img1_00.yuv --InputFile=img1_00.bmp --SourceWidth=160 --SourceHeight=240
# ./TAppEncoderStatic -c 265_encoder_lowdelay_P_main.cfg --ReconFile=re_img1_00.yuv --InputFile=img1_00.bmp --SourceWidth=160 --SourceHeight=240
# ./TAppEncoderStatic -c encoder_intra_main.cfg --ReconFile=re_img1_00.yuv --InputFile=img1_00.yuv --SourceWidth=160 --SourceHeight=240


# ffmpeg -s 160x240 -pix_fmt yuv420p -i re_img1_00.yuv re_img1_00.bmp
