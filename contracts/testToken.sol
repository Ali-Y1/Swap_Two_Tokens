// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract tokenA is ERC20 {
    constructor(uint256 initialSupply) ERC20("usdc", "US") {
        _mint(msg.sender, initialSupply);
    }
}

contract tokenB is ERC20 {
    constructor(uint256 initialSupply) ERC20("usdt", "UT") {
        _mint(msg.sender, initialSupply);
    }
}