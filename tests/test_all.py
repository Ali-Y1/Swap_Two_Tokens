from scripts.helpful_scripts import get_account
from scripts.deploy_testTokens import deploy_tokenA, deploy_tokenB
from scripts.deploy_token import deploy as deploy_token
from scripts.deploy_SwapContract import deploy as deploy_contract

decimals = 18

def test_can_Deploy():
    account = get_account()
    tokenA = deploy_tokenA()
    tokenB = deploy_tokenB()
    MyToken = deploy_token()
    Swap = deploy_contract(tokenA, tokenB, MyToken)

    MyToken.transfer(Swap.address, 100 * 10 ** decimals, {"from": account})
    tokenA.transfer(Swap.address, 100 * 10 ** decimals, {"from": account})
    tokenB.transfer(Swap.address, 100 * 10 ** decimals, {"from": account})

    assert tokenA.balanceOf(Swap.address) == 100 * 10 ** decimals
    assert tokenB.balanceOf(Swap.address) == 100 * 10 ** decimals
    assert MyToken.balanceOf(Swap.address) == 100 * 10 ** decimals


def test_swap():
    account = get_account()
    tokenA = deploy_tokenA()
    tokenB = deploy_tokenB()
    MyToken = deploy_token()
    Swap = deploy_contract(tokenA, tokenB, MyToken)

    MyToken.transfer(Swap.address, 100 * 10 ** decimals, {"from": account})
    tokenA.transfer(Swap.address, 2000 * 10 ** decimals, {"from": account})
    tokenB.transfer(Swap.address, 2000 * 10 ** decimals, {"from": account})

    assert tokenA.balanceOf(Swap.address) == 2000 * 10 ** decimals
    assert tokenB.balanceOf(Swap.address) == 2000 * 10 ** decimals

    amount = 1000 * 10 ** decimals

    print(f"Swap Price: {Swap.getSwapPrice()}")

    tokenA.approve(Swap.address, amount, {"from": account})
    Swap.swap(tokenA.address, amount, {"from": account})
    print(f"TokenA:{tokenA.balanceOf(Swap.address)} ---- TokenB: {tokenB.balanceOf(Swap.address)}")
    assert tokenA.balanceOf(Swap.address) / 10 ** decimals == 3000
    assert round(tokenB.balanceOf(Swap.address) / 10 ** decimals,1) == 998.8


def test_reward():
    account = get_account()
    tokenA = deploy_tokenA()
    tokenB = deploy_tokenB()
    MyToken = deploy_token()
    Swap = deploy_contract(tokenA, tokenB, MyToken)

    MyToken.transfer(Swap.address, 200 * 10 ** decimals, {"from": account})
    tokenA.transfer(Swap.address, 300 * 10 ** decimals, {"from": account})
    tokenB.transfer(Swap.address, 300 * 10 ** decimals, {"from": account})

    assert tokenA.balanceOf(Swap.address) == 300 * 10 ** decimals
    assert tokenB.balanceOf(Swap.address) == 300 * 10 ** decimals

    amount = 200 * 10 ** decimals
    user_balance = MyToken.balanceOf(account.address)

    tokenA.approve(Swap.address, amount, {"from": account})
    Swap.swap(tokenA.address, amount, {"from": account})

    assert MyToken.balanceOf(account.address) == user_balance + 50 * 10 ** decimals
    assert MyToken.balanceOf(Swap.address) == 150 * 10 ** decimals
