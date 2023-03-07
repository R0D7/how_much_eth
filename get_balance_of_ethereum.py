from web3 import Web3

def get_balance_of_eth(wallet_eth):
    # Insert your Ethereum node provider url instead of "ethereum_node_provider_url"
    web3 = Web3(Web3.HTTPProvider("ethereum_node_provider_url"))
    # Get the balance of the wallet 
    balance_wei = float((web3.eth.get_balance(wallet_eth)))
    # Convert the balance (wei) in ether
    balance_ether = float(web3.fromWei(balance_wei, 'ether'))
    return float(balance_ether)
