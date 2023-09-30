# ========== ssh ==========

#ssh-keygen -t ed25519 -C "ferdinand.mom@epita.fr"
#eval "$(ssh-agent -s)"
#ssh-add ~/.ssh/id_ed25519

#git config --global user.email "ferdinand.mom@epita.fr"
#git config --global user.name "Ferdinand Mom"

# ========== Bash ==========
# ls autocomplete
#echo "bind 'set show-all-if-ambiguous on'" >> ~/.bashrc
#echo "bind 'TAB:menu-complete'" >> ~/.bashrc

# Fuzzer
#echo "# Fuzzer" >>  ~/.bashrc
#echo "[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh" >> ~/.bashrc

# Pyenv
#export PYENV_ROOT="$HOME/.pyenv"
#echo "command -v pyenv >/dev/null || export PATH=\"$PYENV_ROOT/bin:$PATH\"" >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
