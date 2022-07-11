### EXPORT ###
export EDITOR='nano'
export VISUAL='nano'
export HISTCONTROL=ignoreboth:erasedups
export PAGER='most'

#PS1='[\u@\h \W]\$ '
PS1='\[\e[0;1;38;5;27m\]\h \[\e[0;1;38;5;31m\][ \[\e[0;1;38;5;31m\]\w \[\e[0;1;38;5;31m\]] \[\e[0;1m\]> \[\e[0;1;38;5;29m\]$(git branch 2>/dev/null | grep '"'"'^*'"'"' | colrm 1 2)\n\[\e[0;1m\]\$ \[\e[0m\]'

# If not running interactively, don't do anything
[[ $- != *i* ]] && return


if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

#ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

### ALIASES ###

#list
alias ls='ls --color=auto'
alias la='lsd -a'
alias ll='lsd -lFh'
alias lll='lsd -alFh'
alias l='lsd'
alias l.="lsd -A | egrep '^\.'"

#fix obvious typo's
alias cd..='cd ..'
alias pdw='pwd'

#grub update
alias update-grub="sudo grub-mkconfig -o /boot/grub/grub.cfg"

# # usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   tar xf $1    ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

[[ -f ~/.bashrc-personal ]] && . ~/.bashrc-personal

echo ""
# reporting tools - install when not installed
neofetch
#screenfetch
#alsi
#paleofetch
#fetch
#hfetch
#sfetch
#ufetch
#ufetch-arco
#pfetch
#sysinfo
#sysinfo-retro
#cpufetch
#colorscript random

#Keyboard and Wallpaper
alias latam='setxkbmap latam && echo "Keyboard set latam"'
alias us='setxkbmap us && echo "Keyboard set us"'

alias off='shutdown -h now'

#My paths
PATH=$PATH:/opt/lampp/bin/
PATH=$PATH:/home/gary/.config/composer/vendor/bin/

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
alias sudo-sync='sudo sync && sudo sysctl -w vm.drop_caches=3 && sudo sync'

alias xampp-start='sudo /opt/lampp/xampp startapache && sudo /opt/lampp/xampp startmysql'
alias xampp-stop='sudo /opt/lampp/xampp stop'
alias xampp-status='sudo /opt/lampp/xampp status'
alias psql-start='sudo systemctl start postgresql-10 && echo "Postgresql started"'
alias psql-stop='sudo systemctl stop postgresql-10 && echo "Postgresql stoped"'
alias psql-status='echo "PostgreSql status: " && sudo systemctl is-active postgresql-10'
alias php-v='php -v'
alias php-7='export PATH=/opt/lampp/bin:$PATH && echo "php version changed to php7"'
alias php-8='export PATH=/usr/bin:$PATH && echo "php version changed to php8"'
alias ky='cat ~/.ky'
alias win-on='sudo mount /dev/nvme0n1p2 /mnt/win11/ && thunar /mnt/win11'
alias win-off='sudo umount /mnt/win11/'
alias xampp='sudo /opt/lampp/manager-linux-x64.run'
alias sysinfo='echo "*******************" && echo "*** osysinfo -f ***" && echo "*******************" && osysinfo -f'
