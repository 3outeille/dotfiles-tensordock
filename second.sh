# ===== Vim =====
sudo apt install vim

# ====== Fuzzer Finder =====
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install

# ======= Pdbpp =========
rm $HOME/.pdbrc.py
rm $HOME/.pdbrc

ln -s $HOME/dotfiles/config/pdbrc.py $HOME/.pdbrc.py
ln -s $HOME/dotfiles/config/pdbrc $HOME/.pdbrc

# ======= Pyenv =======
curl https://pyenv.run | bash
sudo apt-get install build-essential zlib1g-dev libffi-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev liblzma-dev
sudo apt-get install python3-zipp # for tiktoken
sudo apt-get install python3-dev  # for torch-compile

# ======== Nvtop ======
# https://github.com/Syllo/nvtop/issues/51#issuecomment-759600674
sudo apt install libdrm-dev libsystemd-dev
sudo apt install cmake libncurses5-dev libncursesw5-dev git
git clone https://github.com/Syllo/nvtop.git
mkdir -p nvtop/build && cd nvtop/build
cmake .. -DNVIDIA_SUPPORT=ON -DAMDGPU_SUPPORT=ON -DINTEL_SUPPORT=ON
make
sudo make install

cd ~

