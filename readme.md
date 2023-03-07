# Ethereum Wallet Value
This program allows you to determine the value in USD of the Ethereum held in a given wallet. It is composed of three files:

* free_baby_nansen.py: the main file that prompts the user for an Ethereum address and displays the corresponding USD value of the Ethereum held in that wallet.
* get_balance_of_ethereum.py: a module that retrieves the balance of an Ethereum wallet and converts it from Wei to Ether.
* get_ethereum_price.py: a module that retrieves the current price of Ethereum in USD from the CoinMarketCap API.

## Requirements
To use this program, you will need to have an Ethereum node provider and a CoinMarketCap API key.

## Usage
1. Clone this repository to your local machine.
2. Open the get_balance_of_ethereum.py file and replace 'node provider url' (line 5) with the URL of your Ethereum node provider.
3. Open the get_ethereum_price.py file and replace 'API_KEY' with your CoinMarketCap API (line 13) key.
4. Open the terminal and navigate to the directory where you cloned this repository.
5. Run the command python3 free_baby_nansen.py.
6. Enter an Ethereum address when prompted.
The program will display the corresponding USD value of the Ethereum held in the wallet.

## Example
```python
Enter an Ethereum address: 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
The wallet has 1070.5062810628 $ of Ethereum
```

## Dependencies
* [web3](https://web3py.readthedocs.io/en/v5/)
* [requests](https://docs.python-requests.org/en/latest/)
