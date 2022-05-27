from brownie import Swap,config,network
from scripts.helpful_scripts import get_account
from web3 import Web3

def deploy(tokenA,tokenB,myToken):
    account = get_account()
    swap = Swap.deploy(tokenA,tokenB,config['networks'][network.show_active()]['usdc_usd_price_feed'],config['networks'][network.show_active()]['usdt_usd_price_feed'],myToken, {"from": account})
    print(" Deployed")
    return swap


