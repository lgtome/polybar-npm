#! /bin/bash

polybar_dir="~/.config/polybar"
polybar_conf="./pnpm.conf"
python_file="./pnpm.py"
python_config="./pnpm.py"
fonts_local_dir="./fonts"
fonts_dir="~/.local/share/fonts"


mkdir -p $polybar_dir
mkdir -p $fonts_dir

mv "$fonts_local_dir/*.ttf" $fonts_dir

fc-cache -fv $fonts_dir

mv -t "$polybar_dir/pnpm" $python_file $python_config

mv $polybar_conf $polybar_dir

echo "Installation successed. You just need to include module in the polybar config file, just follow readme"