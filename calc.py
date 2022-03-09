import random
import sys
import calendar
from datetime import *

def show_menu():
    print("LIST MENU")
    print("1. hitung jarak/kecepatan/jarak tempuh")
    print("2. menghitung margin untung rugi")
    print("3. menghitung diskon")
    print("4. menghitung luas dan keliling lingkaran")
    print("5. exit")
    print("6. youtube downloader")
    print("7. game gunting batu kertas")
    print("8. game tebak angka")
    print("9. blackjack")
    print("10. hitung usia")
    choice = input("pilihan anda : ")
    if choice == "1" :
        print("")
        hitung_svt()
    elif choice == "2" :
        print("")
        hitung_margin()
    elif choice == "3":
        print("")
        hitung_diskon()
    elif choice == "4":
        print("")
        hitung_luas_dan_keliling_lingkaran()
    elif choice == "5":
        exit()
    elif choice == "6":
        print("")
        youtube_downloader()
    elif choice == "7":
        print("")
        gbk()
    elif choice == "8":
        print("")
        game_tebak_angka()
    elif choice == "9":
        print("")
        blackjack()
    elif choice == "10":
        print(" ")
        usia()
    else:
        print("salah pilih ya kk... pilih lagi yuk")
        print("")
        show_menu()

def hitung_svt():
    S = float(input("jarak (0 jika tidak diketahui) = "))
    t = float(input("waktu dalam menit (0 jika tidak diketahui) = "))
    V = float(input("kecepatan (0 jika tidak diketahui) = "))
    T = float(t/60)
    if S == 0:
        rumus = V*T
        print("rumus jarak tempuh adalah (waktu x kecepatan) = ", V, "x", T, "=", rumus)
        print("jadi jarak tempuhnya adalah = ", rumus, "km")
        print("1. menu ")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print("")
            show_menu()
        elif menu == "2":
            exit()
    
    elif T == 0:
        rumus1 = S/V
        rumus2 = round(rumus1, 2)
        menit = rumus1*60
        menit2 = round(menit, 2)
        print("waktu tempuhnya adalah = ",rumus2, "Jam", "(",menit2, "menit)")
        print("udah kelar nih kk hitungannya")
        print("1. menu ")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print("")
            show_menu()
        elif menu == "2":
            exit()
            
    elif V == 0:
        rumusV = round(S/T, 2)
        print("kecepatan tetapnya adalah = ",rumusV, "Kmh")
        print("udah kelar nih kk hitungannya")
        print("1. menu ")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print("")
            show_menu()
        elif menu == "2":
            exit()

def hitung_margin():
    BIAYA_MODAL = float(input("biaya modal = "))
    HARGA_JUAL = float(input("harga jual = "))
    KEUNTUNGAN = float(HARGA_JUAL - BIAYA_MODAL)   
    persentase_markup = round(((KEUNTUNGAN/BIAYA_MODAL)*100), 2)
    if KEUNTUNGAN == 0:
        print("maaf anda mendapatkan", KEUNTUNGAN, "keuntungan karena harga jual anda = biaya modal anda")
        print("anda mendapatkan", persentase_markup,"% keuntungan")
        print("udah kelar nih kk hitungannya")
        print("1. menu ")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print("")
            show_menu()
        elif menu == "2":
            exit()
            
    if KEUNTUNGAN > 0:
        print(str("Keuntungan = "),KEUNTUNGAN)
        print(str("markup = "), persentase_markup,"%")
        print("udah kelar nih kk hitungannya")
        print("1. menu ")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print("")
            show_menu()
        elif menu == "2":
            exit()
            
    elif KEUNTUNGAN < 0:
        print("maaf anda rugi", KEUNTUNGAN)
        print("anda rugi", persentase_markup, "%")
        print("udah kelar nih kk hitungannya")
        print("1. menu ")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print("")
            show_menu()
        elif menu == "2":
            exit()
    
def hitung_diskon():
    harga_awal = float(input("masukan harga sebelum diskon (0 jika tidak diketahui) = "))
    harga_jual = float(input("masukan harga setelah diskon (0 jika tidak diketahui) = "))
    diskon = float(input("masukan besaran diskon (0 jika tidak diketahui) = "))
    
    if diskon == 0:
        selisih_harga = harga_awal - harga_jual
        diskon = round(float((selisih_harga/harga_awal)*100), 2)
        print("besar persentase diskonnya adalah = ", diskon, "%")
        print("1. hitung lagi ?")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print("")
            show_menu()
        elif menu == "2":
            exit()
            
    elif harga_awal == 0:
        selisihdiskon = 100 - diskon
        hargaawal = round(float((harga_jual*100)/selisihdiskon), 2)
        print("harga awal sebelum diskon adalah = ", hargaawal)
        print("1. hitung lagi ?")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print("")
            show_menu()
        elif menu == "2":
            exit()
            
    elif harga_jual == 0:
        HJ = round(float(harga_awal - (harga_awal*(diskon/100))))
        print("harga setelah diskonnya adalah = ", HJ)
        print("udah kelar nih kk hitungannya")
        print("1. hitung lagi ?")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print("")
            show_menu()
        elif menu == "2":
            exit()
    
def hitung_luas_dan_keliling_lingkaran():
    r = float(input("jari-jari (jari-jari adalah 1/2 dari diameter silahkan masukan dalam satuan cm) = "))
    phi = float(22/7)
    k = round(float(2*phi*r), 2)
    K = round(float(phi*(r**2)), 2)
    print("keliling lingkarannya adalah = ", k, "cm" )
    print("luas lingkarannya adalah = ", K, "cm**2")
    print("udah kelar nih kk hitungannya")
    print("1. hitung lagi ?")
    print("2. exit")
    menu = input("pilih : ")
    if menu == "1":
        print("")
        show_menu()
    elif menu == "2":
        exit()

def hitung_luas_dan_keliling_segitiga():
    A = float(input("alas segitiga = "))
    T = float(input("tinggi segitiga = "))
    rumus = round(float((1/2)*A*T), 2)
    print("luas segitiganya adalah = ", rumus, "cm**2")
    print("udah kelar nih kk hitungannya")
    print("1. hitung lagi ?")
    print("2. exit")
    menu = input("pilih : ")
    if menu == "1":
        print("")
        show_menu()
    elif menu == "2":
        exit()
        
def youtube_downloader():
    from pytube import YouTube

    link = input("Enter the link of YouTube video you want to download:  ")
    yt = YouTube(link)

    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)
    print("Rating of video: ",yt.rating)

    ys = yt.streams.get_highest_resolution()

    print("Downloading...")
    ys.download()
    print("Download completed!!")
    print("1. download lagi ?")
    print("2 kembali ke menu utama ?")
    print("3. exit")
    menu = input("pilih : ")
    if menu == "1":
        youtube_downloader()
    elif menu == "2":
        print("")
        show_menu()
    elif menu == "3":
        exit()

def gbk():
    menang = 0
    kalah = 0
    seri = 0
    while True: # The main game loop.
        print('%s Menang, %s Kalah, %s Seri' % (menang, kalah, seri))
        while True: # The player input loop.
            print('Enter your move: (g)unting (b)atu (k)ertas atau (m)enu')
            playerMove = input()
            if playerMove == 'm':
                print("")
                show_menu() # Quit the program.
            elif playerMove == 'g' or playerMove == 'b' or playerMove == 'k':
                break # Break out of the player input loop.
            print('Type one of g, b, k, or q.')
        # Display what the player chose:
        if playerMove == 'g':
            print('GUNTING versus...')
        elif playerMove == 'b':
            print('BATU versus...')
        elif playerMove == 'k':
            print('KERTAS versus...')
        # Display what the computer chose:
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            computerMove = 'g'
            print('GUNTING')
        elif randomNumber == 2:
            computerMove = 'b'
            print('BATU')
        elif randomNumber == 3:
            computerMove = 'k'
            print('KERTAS')
        # Display and record the win/loss/tie:
        if playerMove == computerMove:
            print('Kita seri ya!')
            seri = seri + 1
        elif playerMove == 'b' and computerMove == 'g':
            print('Kamu Menang!')
            menang = menang + 1
        elif playerMove == 'k' and computerMove == 'b':
            print('Kamu Menang!')
            menang = menang + 1
        elif playerMove == 'g' and computerMove == 'k':
            print('Kamu Menang!')
            menang = menang + 1
        elif playerMove == 'b' and computerMove == 'k':
            print('Kamu Kalah!')
            kalah = kalah + 1
        elif playerMove == 'k' and computerMove == 'g':
            print('Kamu Kalah!')
            kalah = kalah + 1
        elif playerMove == 'g' and computerMove == 'b':
            print('Kamu Kalah!')
            kalah = kalah + 1

def game_tebak_angka():
    angka = random.randint(1, 27)
    print("aku sedang memikirkan sebuah angka antara 1 dan 27")
    print("aku kasih 6 kesempatan buat nebak angka yang aku pikirkan ya")
    for tebakan in range(1, 7):
        tebak = int(input("tebakanmu : "))
        if tebak < angka:
            print("tebakanmu terlalu kecil")
        elif tebak > angka:
            print("tebakanmu terlalu besar")
        else:
            break
    if tebak == angka:
        print("tebakanmu benar dalam", tebakan, "kali tebak")
        print("")
        show_menu()
    else:
        print("tebakanmu salah semua, angka yang aku pikirkan adalah", str(angka))
        print("")
        show_menu()

def blackjack():
    HEARTS   = chr(9829) # Character 9829 is '♥'.
    DIAMONDS = chr(9830) # Character 9830 is '♦'.
    SPADES   = chr(9824) # Character 9824 is '♠'.
    CLUBS    = chr(9827) # Character 9827 is '♣'.
    BACKSIDE = 'backside'


    def main():
        print('''Blackjack, by Al Sweigart al@inventwithpython.com

        Rules:
          Try to get as close to 21 without going over.
          Kings, Queens, and Jacks are worth 10 points.
          Aces are worth 1 or 11 points.
          Cards 2 through 10 are worth their face value.
          (H)it to take another card.
          (S)tand to stop taking cards.
          On your first play, you can (D)ouble down to increase your bet
          but must hit exactly one more time before standing.
          In case of a tie, the bet is returned to the player.
          The dealer stops hitting at 17.''')

        money = 10000
        while True:  # Main game loop.
            # Check if the player has run out of money:
            if money <= 0:
                print("You're broke!")
                print("Good thing you weren't playing with real money.")
                print('Thanks for playing!')
                sys.exit()

            # Let the player enter their bet for this round:
            print('Money:', money)
            bet = getBet(money)

            # Give the dealer and player two cards from the deck each:
            deck = getDeck()
            dealerHand = [deck.pop(), deck.pop()]
            playerHand = [deck.pop(), deck.pop()]

            # Handle player actions:
            print('Bet:', bet)
            while True:  # Keep looping until player stands or busts.
                displayHands(playerHand, dealerHand, False)
                print()

                # Check if the player has bust:
                if getHandValue(playerHand) > 21:
                    break

                # Get the player's move, either H, S, or D:
                move = getMove(playerHand, money - bet)

                # Handle the player actions:
                if move == 'D':
                    # Player is doubling down, they can increase their bet:
                    additionalBet = getBet(min(bet, (money - bet)))
                    bet += additionalBet
                    print('Bet increased to {}.'.format(bet))
                    print('Bet:', bet)

                if move in ('H', 'D'):
                    # Hit/doubling down takes another card.
                    newCard = deck.pop()
                    rank, suit = newCard
                    print('You drew a {} of {}.'.format(rank, suit))
                    playerHand.append(newCard)

                    if getHandValue(playerHand) > 21:
                        # The player has busted:
                        continue

                if move in ('S', 'D'):
                    # Stand/doubling down stops the player's turn.
                    break

            # Handle the dealer's actions:
            if getHandValue(playerHand) <= 21:
                while getHandValue(dealerHand) < 17:
                    # The dealer hits:
                    print('Dealer hits...')
                    dealerHand.append(deck.pop())
                    displayHands(playerHand, dealerHand, False)

                    if getHandValue(dealerHand) > 21:
                        break  # The dealer has busted.
                    input('Press Enter to continue...')
                    print('\n\n')

            # Show the final hands:
            displayHands(playerHand, dealerHand, True)

            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)
            # Handle whether the player won, lost, or tied:
            if dealerValue > 21:
                print('Dealer busts! You win ${}!'.format(bet))
                money += bet
            elif (playerValue > 21) or (playerValue < dealerValue):
                print('You lost!')
                money -= bet
            elif playerValue > dealerValue:
                print('You won ${}!'.format(bet))
                money += bet
            elif playerValue == dealerValue:
                print('It\'s a tie, the bet is returned to you.')

            input('Press Enter to continue...')
            print('\n\n')


    def getBet(maxBet):
        """Ask the player how much they want to bet for this round."""
        while True:  # Keep asking until they enter a valid amount.
            print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
            bet = input('> ').upper().strip()
            if bet == 'QUIT':
                print('Thanks for playing!')
                sys.exit()

            if not bet.isdecimal():
                continue  # If the player didn't enter a number, ask again.

            bet = int(bet)
            if 1 <= bet <= maxBet:
                return bet  # Player entered a valid bet.


    def getDeck():
        """Return a list of (rank, suit) tuples for all 52 cards."""
        deck = []
        for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
            for rank in range(2, 11):
                deck.append((str(rank), suit))  # Add the numbered cards.
            for rank in ('J', 'Q', 'K', 'A'):
                deck.append((rank, suit))  # Add the face and ace cards.
        random.shuffle(deck)
        return deck


    def displayHands(playerHand, dealerHand, showDealerHand):
        """Show the player's and dealer's cards. Hide the dealer's first
        card if showDealerHand is False."""
        print()
        if showDealerHand:
            print('DEALER:', getHandValue(dealerHand))
            displayCards(dealerHand)
        else:
            print('DEALER: ???')
            # Hide the dealer's first card:
            displayCards([BACKSIDE] + dealerHand[1:])

        # Show the player's cards:
        print('PLAYER:', getHandValue(playerHand))
        displayCards(playerHand)


    def getHandValue(cards):
        """Returns the value of the cards. Face cards are worth 10, aces are
        worth 11 or 1 (this function picks the most suitable ace value)."""
        value = 0
        numberOfAces = 0

        # Add the value for the non-ace cards:
        for card in cards:
            rank = card[0]  # card is a tuple like (rank, suit)
            if rank == 'A':
                numberOfAces += 1
            elif rank in ('K', 'Q', 'J'):  # Face cards are worth 10 points.
                value += 10
            else:
                value += int(rank)  # Numbered cards are worth their number.


        value += numberOfAces  
        for i in range(numberOfAces):

            if value + 10 <= 21:
                value += 10

        return value


    def displayCards(cards):
        """Display all the cards in the cards list."""
        rows = ['', '', '', '', '']  

        for i, card in enumerate(cards):
            rows[0] += ' ___  '  
            if card == BACKSIDE:
                # Print a card's back:
                rows[1] += '|## | '
                rows[2] += '|###| '
                rows[3] += '|_##| '
            else:
                rank, suit = card  # The card is a tuple data structure.
                rows[1] += '|{} | '.format(rank.ljust(2))
                rows[2] += '| {} | '.format(suit)
                rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

        # Print each row on the screen:
        for row in rows:
            print(row)


    def getMove(playerHand, money):
        """Asks the player for their move, and returns 'H' for hit, 'S' for
        stand, and 'D' for double down."""
        while True:  # Keep looping until the player enters a correct move.
            # Determine what moves the player can make:
            moves = ['(H)it', '(S)tand']

            # The player can double down on their first move, which we can
            # tell because they'll have exactly two cards:
            if len(playerHand) == 2 and money > 0:
                moves.append('(D)ouble down')

            # Get the player's move:
            movePrompt = ', '.join(moves) + '> '
            move = input(movePrompt).upper()
            if move in ('H', 'S'):
                return move  # Player has entered a valid move.
            if move == 'D' and '(D)ouble down' in moves:
                return move  # Player has entered a valid move.


    # If the program is run (instead of imported), run the game:
    if __name__ == '__main__':
        main()

def hitung_harga_satuan():
    harga = int(input("masukan harga beli : "))
    jumlah = int(input("masukan jumlah satuan barang : "))
    hargasatuan = harga/jumlah
    persentaseuntung = float(input("masukan besaran untung yang diinginkan : "))
    untung = int(harga * (persentaseuntung / 100))
    hargajual = (harga + untung)/jumlah
    hargajual_total = harga + untung
    if jumlah > 1:
        print("harga satuannya adalah : ", hargasatuan)
        print("harga jual per kotaknya adalah :", hargajual_total)
        print("untung anda adalah ", untung, "total")
        print("harga jual satuan ", hargajual) 
        print("udah kelar nih kk hitungannya")
        print("1. menu")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print(" ")
            show_menu()
        elif menu == "2":
            exit()
            
    elif jumlah == 1:
        print("harga jual kembalinya adalah :", hargajual_total)
        print("untung anda", untung, "total")
        print("udah kelar nih kk hitungannya")
        print("1. menu")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print(" ")
            show_menu()
        elif menu == "2":
            exit()
            
def usia():
    tahun = int(input("masukan tahun lahir : "))
    for Bulan_Lahir in range(1, 4):
        bulan_lahir = int(input("masukan bulan lahir(dalam angka) : "))
        if bulan_lahir > 12:
            print("maaf bulan hanya ada 12")
        else:
            break
    for TanggaL in range (1, 4):
        tanggal = int(input("masukan tanggal lahir : "))
        if tanggal > 31:
            print("maaf salah tanggal")
        else:
            break
    print(" ")
    sekarang = datetime.now()
    tanggal_lahir = datetime(tahun, bulan_lahir, tanggal)
    usia = sekarang.year - tahun
    if sekarang.month >= bulan_lahir:
        tanggal_ini = sekarang.strftime("%A, %d %b %Y, %I:%M:%S %p")
        print(calendar.month(tahun, bulan_lahir))
        print("     |\/|")
        print("     |  |")
        print("      \/")
        print("      ||", usia, "tahun")
        print("     _||_")
        print("     \  /")
        print("      \/")
        print(calendar.month(sekarang.year, sekarang.month))
        print("pada hari ini", tanggal_ini, "anda berusia", usia, "tahun",'\n')
        print("udah kelar nih kk hitungannya")
        print("1. menu")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print(" ")
            show_menu()
        elif menu == "2":
            exit()
    else:
        usia1 = usia - 1
        tanggal_ini = sekarang.strftime("%A, %d %b %Y, %I:%M:%S %p")
        print(calendar.month(tahun, bulan_lahir))
        print("     |\/|")
        print("     |  |")
        print("      \/")
        print("      ||", usia1, "tahun")
        print("     _||_")
        print("     \  /")
        print("      \/")
        print(calendar.month(sekarang.year, sekarang.month))
        print("pada hari ini", tanggal_ini, "anda berusia", usia1, "tahun",'\n')
        print("udah kelar nih kk hitungannya")
        print("1. menu")
        print("2. exit")
        menu = input("pilih : ")
        if menu == "1":
            print(" ")
            show_menu()
        elif menu == "2":
            exit()
            
print("""welcome to pandabear app 
hanya PANDA yang dapat mengakses program ini""")
for passwordInput in range(1, 4):
    password = input("masukan password : ").upper()
    if password == "PANDA":
        print("")
        show_menu()


"""salam hangat dari 88kumaisbear88 
code ini saya tulis secara spontan dan pada saat saya sedang bosan, 
jadi jika terdapat error pada program ini, saya mohon maaf sebesarnya,
mari bermain sekaligus belajar python"""