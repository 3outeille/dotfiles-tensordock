# ===== Zsh ====
# Link zsh
rm $HOME/.zshrc
ln -s $HOME/dotfiles-tensordock/config/zshrc $HOME/.zshrc

rm -rf $HOME/.zsh
mkdir -p $HOME/.zsh
ln -s $HOME/dotfiles-tensordock/config/aliases.zsh $HOME/.zsh/aliases.zsh

# Change shell to zsh
yes | sudo chsh -s $(which zsh)

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
mv zsh-syntax-highlighting ${HOME}/.oh-my-zsh/plugins


# ===== Vim =====
yes | sudo apt install vim

# ====== Fuzzer Finder =====
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
yes | ~/.fzf/install

# ======= Pdbpp =========
rm $HOME/.pdbrc.py
rm $HOME/.pdbrc

ln -s $HOME/dotfiles-tensordock/config/pdbrc.py $HOME/.pdbrc.py
ln -s $HOME/dotfiles-tensordock/config/pdbrc $HOME/.pdbrc

# ======== Nvtop ======
# https://github.com/Syllo/nvtop/issues/51#issuecomment-759600674
yes | sudo apt install libdrm-dev libsystemd-dev
yes | sudo snap install cmake --classic
yes | sudo ln -s /snap/bin/cmake /usr/bin/cmake
yes | sudo apt install libncurses5-dev libncursesw5-dev git
git clone https://github.com/Syllo/nvtop.git
mkdir -p nvtop/build && cd nvtop/build
cmake .. -DNVIDIA_SUPPORT=ON -DAMDGPU_SUPPORT=ON -DINTEL_SUPPORT=ON
make
yes | sudo make install

cd ~

# ====== Expman =========
git clone https://github.com/megvii-research/expman $HOME/.expman
echo '[[ -o interactive ]] && source $HOME/.expman/expman.zsh' >> ~/.zshrc

# ======= vscode extension ==========
ln -s $HOME/dotfiles-tensordock/config/vscode-server/extensions $HOME/.vscode-server/extensions
