from web3 import Web3
from get_eth_price import get_eth_price_
from get_balance_of_ethereum import get_balance_of_eth

i = True
while i is True :
    eth_wallet = input("Enter an ethereum adress : ")
    #Verify if the adress format is the address formats is recognize
    if Web3.isAddress(eth_wallet) is True :

        print("The wallet has", get_balance_of_eth(eth_wallet)*get_eth_price_(), "$ of Ethereum")
        print("----------------------------------------")
    else : print("Invalid adress")