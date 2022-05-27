from brownie import MyToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initialSupply = Web3.toWei(10000, "ether")


def deploy():
    account = get_account()
    token = MyToken.deploy(initialSupply, {"from": account})
    print(f"{token.name()} is deployed")
    return token


def main():
    deploy()
