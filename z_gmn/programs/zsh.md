1) საჭირო ინსტრუმენტების დაყენება
​ჯერ დავაყენოთ თავად zsh და curl, რომელიც ფაილების
 გადმოსაწერად გვჭირდება:
pkg update && pkg upgrade
pkg install zsh curl git

2)  Oh My Zsh-ის ინსტალაცია
​ახლა გაუშვი ეს "გრძელი" ბრძანება, რომელიც ყველაფერს
 ავტომატურად გააკეთებს:
sh -c "$(curl -fsSL https://raw.githubusercontent.com
/ohmyzsh/ohmyzsh/master/tools/install.sh)"

3. "ჭკვიანი" პლაგინების დამატება (ყველაზე მაგარი ნაწილი!)
​რომ ტერმინალმა თავად გიკარნახოს ბრძანებები
 (როგორც Fish-ში), დავაყენოთ ეს ორი პლაგინი:
​ავტომატური კარნახი (Autosuggestions):

git clone https://github.com/zsh-users/zsh-autosuggestions
 ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/
zsh-autosuggestions

ფერადი ბრძანებები (Syntax Highlighting):

git clone https://github.com/zsh-users/
zsh-syntax-highlighting.git ${ZSH_CUSTOM:
-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

4. ყველაფრის გააქტიურება
​ახლა ეს პლაგინები უნდა "ჩავრთოთ" .zshrc ფაილში:
​გახსენი ფაილი: nano ~/.zshrc
​მოძებნე ხაზი, სადაც წერია plugins=(git).
​შეცვალე ასე:
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
​შეინახე (Ctrl+O, Enter) და გამოდი (Ctrl+X).
​5. ფინალი
​ბოლოს, აკრიფე:
source ~/.zshrc

