from brownie import tokenA, tokenB
from scripts.helpful_scripts import get_account
from web3 import Web3

initialSupply = Web3.toWei(10000, "ether")


def deploy_tokenA():
    account = get_account()
    token = tokenA.deploy(initialSupply, {"from": account})
    print(f"{token.name()} is deployed")
    return token


def deploy_tokenB():
    account = get_account()
    token = tokenB.deploy(initialSupply, {"from": account})
    print(f"{token.name()} is deployed")
    return token


def main():
    deploy_tokenA()
    deploy_tokenB()
