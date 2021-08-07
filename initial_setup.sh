#!/usr/bin/bash

create_venv() {
    echo "creating venv"
    virtualenv venv
    echo "activate venv"
    source $(pwd)/venv/bin/activate # && pip3 install youtube_dl
}

if check_venv=$(pip3 list | grep virtualenv)
then
    create_venv
else
    echo "install venv"
    echo $(pip3 install virtualenv)
    create_venv
fi

echo "installing youtube_dl module"
pip3 install -r requirements.txt

touch song_list.txt