from scripts.helpful_scripts import get_account
from scripts.deploy_testTokens import deploy_tokenA, deploy_tokenB
from scripts.deploy_token import deploy as deploy_token
from scripts.deploy_SwapContract import deploy as deploy_contract


def test_can_Deploy():
    account = get_account()
    tokenA = deploy_tokenA()
    tokenB = deploy_tokenB()
    MyToken = deploy_token()
    Swap = deploy_contract(tokenA, tokenB, MyToken)

    MyToken.transfer(Swap.address, 100, {"from": account})
    tokenA.transfer(Swap.address, 100, {"from": account})
    tokenB.transfer(Swap.address, 100, {"from": account})

    assert tokenA.balanceOf(Swap.address) == 100
    assert tokenB.balanceOf(Swap.address) == 100
    assert MyToken.balanceOf(Swap.address) == 100


def test_swap():
    account = get_account()
    tokenA = deploy_tokenA()
    tokenB = deploy_tokenB()
    MyToken = deploy_token()
    Swap = deploy_contract(tokenA, tokenB, MyToken)

    MyToken.transfer(Swap.address, 100, {"from": account})
    tokenA.transfer(Swap.address, 100, {"from": account})
    tokenB.transfer(Swap.address, 100, {"from": account})

    assert tokenA.balanceOf(Swap.address) == 100
    assert tokenB.balanceOf(Swap.address) == 100

    amount = 50

    tokenA.approve(Swap.address, amount, {"from": account})
    Swap.swap(tokenA.address, amount, {"from": account})

    assert tokenA.balanceOf(Swap.address) == 100 + amount
    assert tokenB.balanceOf(Swap.address) == 100 - amount


def test_reward():
    account = get_account()
    tokenA = deploy_tokenA()
    tokenB = deploy_tokenB()
    MyToken = deploy_token()
    Swap = deploy_contract(tokenA, tokenB, MyToken)

    MyToken.transfer(Swap.address, 200, {"from": account})
    tokenA.transfer(Swap.address, 300, {"from": account})
    tokenB.transfer(Swap.address, 300, {"from": account})

    assert tokenA.balanceOf(Swap.address) == 300
    assert tokenB.balanceOf(Swap.address) == 300

    amount = 200
    user_balance = MyToken.balanceOf(account.address)

    tokenA.approve(Swap.address, amount, {"from": account})
    Swap.swap(tokenA.address, amount, {"from": account})

    assert tokenA.balanceOf(Swap.address) == 300 + amount
    assert tokenB.balanceOf(Swap.address) == 300 - amount
    assert MyToken.balanceOf(account.address) == user_balance + 50
    assert MyToken.balanceOf(Swap.address) == 150
