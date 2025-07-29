from crypto_utils import Wallet

my_wallet = Wallet('Donald')
my_wallet.deposit("ETH", 0.7)
print(my_wallet.view_balance())
#wallet = CryptoWallet("donald")
#wallet.deposit("eth", 0.8)
#wallet.deposit("btc", 0.9)

#print(wallet.view_balance())

